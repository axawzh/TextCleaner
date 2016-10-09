import re
from nltk.corpus import word

wordlist_path = './wordlist/words.txt'

stopwords = [
    "a", 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after',
    'afterwards', 'again', 'against', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along',
    'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any',
    'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear',
    'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', 'aside', 'ask', 'asking',
    'associated', 'at', 'available', 'away', 'awfully', 'be', 'became', 'because', 'become', 'becomes',
    'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside',
    'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', "c'mon", "c's",
    'came', 'can', "can't", 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes',
    'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering',
    'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', 'currently',
    'definitely', 'described', 'despite', 'did', "didn't", 'different', 'do', 'does', "doesn't",
    'doing', "don't", 'done', 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'either',
    'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every',
    'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'far',
    'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly',
    'forth', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go',
    'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', "hadn't", 'happens', 'hardly', 'has',
    "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hello', 'help', 'hence', 'her', 'here',
    "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself',
    'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', "i'd", "i'll", "i'm", "i've", 'ie', 'if',
    'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates',
    'inner', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's",
    'its', 'itself', 'just', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately',
    'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely',
    'little', 'look', 'looking', 'looks', 'ltd', 'mainly', 'many', 'may', 'maybe', 'me', 'mean',
    'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my',
    'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither',
    'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor',
    'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
    'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others',
    'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own',
    'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible',
    'presumably', 'probably', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really',
    'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'said',
    'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed',
    'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven',
    'several', 'shall', 'she', 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody',
    'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry',
    'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', "t's", 'take',
    'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's", 'thats',
    'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there's", 'thereafter',
    'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', "they'd", "they'll",
    "they're", "they've", 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though',
    'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward',
    'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'un', 'under',
    'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful',
    'uses', 'using', 'usually', 'value', 'various', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was',
    "wasn't", 'way', 'we', "we'd", "we'll", "we're", "we've", 'welcome', 'well', 'went', 'were',
    "weren't", 'what', "what's", 'whatever', 'when', 'whence', 'whenever', 'where', "where's",
    'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while',
    'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish',
    'with', 'within', 'without', "won't", 'wonder', 'would', "wouldn't", 'yes', 'yet', 'you', "you'd",
    "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'zero']

KNOWN_REPLACEMENTS = [
    ('ﬁ', 'fi'), ('ﬂ', 'fl')
]
formula_pattern = r'\b[^\s]* =( ?[+−]?\w+([\.,]\d+)? ?)([+−×*]( ?\w+(\.\d+)? ?))*( ?= ?[+−]?\d+(\.\d+)?)?\b'
expression_pattern = r'\b( ?[+−]?\w+([\.,]\d+)? ?)([+−×*/]( ?\w+(\.\d+)? ?))+( ?= ?[+−]?\d+(\.\d+)?)?\b'  # formula without '='
function_pattern = r'[ωδ\w]+ ?\([\w ωδ]+\)'
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


def remove_stopwords(string):
    string = ' '.join([word for word in string.split() if word not in stopwords])
    return string


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
    return re.sub(r'\b- \b', '', string)


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
    if not string:
        return string
    have_function = re.search(function_pattern, string)
    have_range = re.search(range_pattern, string)
    if have_function or have_range:
        string = re.sub(function_pattern, '[FORMULA]', string)
        string = re.sub(range_pattern, '[FORMULA]', string)
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
        result_str.append(re.sub(r'(\[FORMULA\]([,.] ?)?){2,}', '[FORMULA]', line))
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
    english_words = set(word.strip() for word in wordlist_file)  # is .lower() needed? -check word.txt


def is_englishword(word):
    return word in english_words


# checking function
def check_english(string):
    result_str = []
    for line in string.strip().splitlines():
        result_line = []
        for word in line.strip().split(" "):
            if is_englishword(word):
                result_line.append(word)
            else:
                result_line.append('[FORMULA]')
        ' '.join(result_line)
        result_str.append(result_line)
    return '\n'.join(result_str)


class Clean():
    methods = [string_validation,
               remove_formula,
               remove_inlineformula,
               join_brokenwords,
               replace_known,
               remove_nonascii,
               merge_placeholder
               ]

    def __init__(self, method_list=[]):
        if (len(method_list) > 0):
            self.methods = method_list

    def clean(self, txt, debug=0):
        for m in self.methods:
            txt = m(txt)
            if debug:
                print('\n\n{}\n\n{}'.format(m, txt))
        return txt


