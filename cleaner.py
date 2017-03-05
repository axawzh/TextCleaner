import re, os

wordlist_path = "./word_list/words.txt"

KNOWN_REPLACEMENTS = [
    ('ﬁ', 'fi'), ('ﬂ', 'fl'), ('``', '"'), ("''", '"'), ('_', '-'), ('–', '-')
]

formula_pattern = r'\b[^\s]* =( ?[+−]?\w+([\.,]\d+)? ?)([+−×*]( ?\w+(\.\d+)? ?))*( ?= ?[+−]?\d+(\.\d+)?)?\b'
expression_pattern = r'\b( ?[+−]?\w+([\.,]\d+)? ?)([+−×*/]( ?\w+(\.\d+)? ?))+( ?= ?[+−]?\d+(\.\d+)?)?\b'  # formula without '='
# function_pattern = r'[ωδ\w]+ ?\([\w ωδ]+\)'
function_pattern = r'\([\w ]+\)'
range_pattern = r'−?(\d+|\w|∞)? [≤≥><] −?(\d+|\w|∞)'

# this regex is used for remove_inlineformula_alt() function
formula_pattern_alt = r'\b([ωδ\w]+ ?\([\w ωδ]+\)|[^\s]* =( ?[+−]?\w+([\.,]\d+)? ?)([+−×*]( ?\w+(\.\d+)? ?))*( ?= ?[+−]?\d+(\.\d+)?)?\b|zzz)'
expression_pattern_alt = r'\b( ?[+−]?\w+([\.,]\w+)? ?)([+−×*/]( ?\w+(\.\d+)? ?))+( ?= ?[+−]?\d+(\.\w+)?)?\b'


def count_endingfullstop(string):
    num_fullstop = 0
    for word in string.strip().split(' '):
        if word.endswith('.'):
            # count only full stop at end of a word (full stop in middle of a word may be a float like 3.2)
            num_fullstop += 1
    return num_fullstop


def is_formula(string):
    if re.search(r'[A-Za-z]{2,}', string):
        return False
    else:
        return True


def replace_known(string):
    for pair in KNOWN_REPLACEMENTS:
        string = string.replace(pair[0], pair[1])
    return string


def remove_formula(string):
    result_str = []
    for line in string.splitlines():
        count = lambda l1, l2: sum([1 for x in l1 if x in l2])
        num_comma = string.count(',')
        num_fullstop = count_endingfullstop(string)
        have_mathoperation = re.search(r'[+−×≤<>≥=≈]+', string)
        if (num_comma + num_fullstop) > 0:
            result_str.append(line)
        else:
            if not have_mathoperation:
                if is_formula(string):
                    result_str.append('[FORMULA]')
                else:
                    result_str.append(line)
            else:
                result_str.append('[FORMULA]')
    return '\n'.join(result_str)


def string_validation(string):
    result_str = []
    for line in string.splitlines():
        if line == '\n' or line.startswith(',') or line.startswith('.') or len(line.split()) == 1:
            result_str.append('')
        else:
            result_str.append(line)
    return '\n'.join(result_str)


def remove_shortwords(string):
    string = re.sub(r'\b\w{1,2}\b', '', string)
    return string


def remove_digits(string):  # replace with space ' '
    string = re.sub(r"\b\d+\b", ' ', string)
    return string


def remove_punctuations(string):  # replace with space ' '
    string = re.sub(r'[^\w\s]', ' ', string)
    return string


def lower_firstword(string):  # lowering the capitalized first letter
    sentences = string.split('. ')
    for i in range(0, len(sentences)):
        try:
            if sentences[i] != '':
                one_sentence = sentences[i].split()
                one_firstword = one_sentence[0]
                if not one_firstword.isupper():  # do not lower the word with full capital letters
                    one_firstword = one_firstword[0].lower() + one_firstword[1:]
                sentences[i] = ' '.join([word for word in one_sentence])
        except:
            print('---error is here---' + str(i) + sentences[i])
    string = ''.join([sentence for sentence in sentences])
    return string


def join_brokenwords(string):  # joining the broken words together
    return re.sub(r'\b-\n\b', '', string)


def remove_inlineformula(string):  # remove formulas that hide inside a sentence
    if not string:
        return string
    # brackets can appear anywhere in a formula,
    # remove the brackets for easier regex matching
    string_nobracket = re.sub(r'[()]+', '', string)
    have_formula = re.search(formula_pattern, string_nobracket)
    have_function = re.search(function_pattern, string)
    if have_formula:
        # the removal of function relies on brackets,
        # therefore if a line contains both function and formula,
        # function must be removed first before formula
        #       if have_function:
        #            string_noformula = re.sub(function_pattern, '[FORMULA]', string)
        #            string_nobracket = re.sub(r'[()]+', '', string_noformula)
        string_noformula = re.sub(formula_pattern, '[FORMULA]', string_nobracket)
        string_noformula = re.sub(expression_pattern, '[FORMULA]', string_noformula)
        return string_noformula
    else:
        return string


# an alternative solution, remove function first, then formula
def remove_inlineformula_alt(string):
    result_str =[]
    for line in string.splitlines():
        have_formula = re.search(formula_pattern_alt, line)
        have_range = re.search(range_pattern, line)
        if have_formula:
            string_noformula = re.sub(formula_pattern_alt, 'zzz', line)
            string_nobracket = re.sub(r'[()]+', '', string_noformula)
            string_noformula = re.sub(formula_pattern_alt, '[FORMULA]', string_nobracket)
            if re.search(expression_pattern, string_noformula):
                string_noformula = re.sub(expression_pattern, '[FORMULA]', string_noformula)
            if have_range:
                string_noformula = re.sub(range_pattern, '[FORMULA]', string_noformula)
            result_str.append(string_noformula)
        if have_range:
            result_str.append(re.sub(range_pattern, '[FORMULA]', line))
        return '\n'.join(result_str)



def remove_inlinefunction(string):  # function like 'f (n)' and 'x (1)'
    have_function = re.search(function_pattern, string)
    if have_function:
        string = re.sub(function_pattern, '[FORMULA]', string)
    return string


def remove_figuretitles(string):
    if not string:
        return string
    num_fullstop = count_endingfullstop(string)
    is_figureortable = string.startswith('Figure ') or string.startswith('Table ')
    if is_figureortable and num_fullstop == 1:
        return '[FIGURE]'
    else:
        return string


def merge_placeholder(string):
    result_str = []
    for line in string.splitlines():
        # line = re.sub(r'(\[NUMERIC\]( |,)*){1,}\[NUMERIC\]', '[NUMERIC]', line)
        # result_str.append(re.sub(r'(\[FORMULA\]( |,)*){1,}\[FORMULA\]', '[FORMULA]', line))
        line = re.sub(r'(\[NUMERIC\]( |,)*){1,}\[NUMERIC\]', '[NUMERIC]', line)
        line = re.sub(r'(\[FORMULA\] ?|\[NUMERIC\] ?)?(\[FORMULA\] ?\[NUMERIC\] ?)+', '[FORMULA]', line)
        line = re.sub(r'\[NUMERIC\] +\[FORMULA\] ?', '[FORMULA]', line)
        result_str.append(re.sub(r'(\[FORMULA\]( |,)*){1,}\[FORMULA\]', '[FORMULA]', line))

    return '\n'.join(result_str)


def remove_nonascii(string):
    string = re.sub(r'[^\x00-\x7F]', '', string)
    return string


def merge_duplicateline(file_str):
    result_str = []
    file_list = file_str.split('\n')
    for line in file_list:
        if len(result_str) == 0 or line != result_str[-1]:
            result_str.append(line)
    return '\n'.join(result_str)

# checking each word in dictionary
# initialization
with open(wordlist_path, 'r') as wordlist_file:
    english_words = set(word.strip().lower() for word in wordlist_file)  # is .lower() needed? -check word.txt


def is_englishword(word):
    return word.lower() in english_words

def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        return False

def remove_double_parentheses(word):
    return re.sub(r'\]\]', ']', word)

# checking function
endingPunctuation = (",", ".", "!", "?", ")", "]")
leadingPunctuation = ("(", "[")
placeholder = ['[FORMULA]', '[NUMERIC]', '[BULLET]']
def check_english(string):
    result_str = []
    stripped_punctuation_left = ''
    stripped_punctuation_right = ''
    for line in string.strip().splitlines():    # Break into lines
        result_line = []
        # for word in line.strip().split(" "):
        for word in re.split(r' |-', line):     # Break into words
            if word in placeholder:             # Do not check placeholders
                result_line.append(word)
            elif word.rstrip(".,!?)") in placeholder:
                result_line.append(word)
            else:
                if word.endswith(endingPunctuation):    # If the word is the last word of the sentence
                    stripped_punctuation_right = word[-1]    # Use hard coding so far, replace if have better method
                    word = word.rstrip(".,!?)]")
                if word.startswith(leadingPunctuation):
                    stripped_punctuation_left = word[0]
                    word = word.lstrip("([")
                if is_englishword(word):
                    result_line.append(stripped_punctuation_left + word + stripped_punctuation_right)
                else:
                    if is_number(word):
                        result_line.append(remove_double_parentheses(stripped_punctuation_left + '[NUMERIC]'+stripped_punctuation_right))
                    else:
                        result_line.append(remove_double_parentheses(stripped_punctuation_left + '[FORMULA]'+stripped_punctuation_right))
            stripped_punctuation_left = ''
            stripped_punctuation_right = ''  # reset to empty to prepare for next loop
        result_str.append(' '.join(result_line))
    return '\n'.join(result_str)


def remove_bullet_pts(text):
    result = []
    for line in text.strip().splitlines():
        new_string = re.sub(r'^(?:[0-9]\)|[a-z]\))|^\d\.\d{0,3}', '[BULLET]', line)
        result.append(new_string)
    return '\n'.join(result)



class Clean(object):
    methods = [string_validation,
               # remove_formula,
               # remove_inlineformula,
               join_brokenwords,
               replace_known,
               remove_nonascii,
               remove_inlinefunction,
               remove_bullet_pts,
               check_english,
               merge_placeholder
               ]

    def __init__(self, method_list=[]):
        if (len(method_list) > 0):
            self.methods = method_list

    def clean(self, txt, path='./output/', file_name='debug.txt', debug=0):
        if debug:
            open(path+file_name, 'w').truncate()
        for m in self.methods:
            txt = m(txt)
            if debug:
                print('\n\n{}\n\n{}'.format(m, txt), file=open(path+file_name, 'a', encoding='UTF-8'))
        return txt

    def clean_server(self, txt):
        for m in self.methods:
            txt = m(txt)
        return txt

    def checksample(self, txt, path='./onput/', file_name_output='checkcorrected.txt', file_name_corrected='correcteddemotext.txt'):
        file = open(path+file_name_corrected, 'r', encoding='UTF-8')
        open(path+file_name_output, 'w').truncate()
        cleaned_line = txt.splitlines()
        corrected_text = file.read().splitlines()
        for i in range(len(cleaned_line)):
            if cleaned_line[i] != corrected_text[i]:
                print('============\nLINE ' + str(i) + '\nCLEAN RESULT: '+cleaned_line[i]\
                      + '\nGROUND TRUTH: ' + corrected_text[i] + '\n============',\
                      file=open(path+file_name_output, 'a', encoding='UTF-8'))


