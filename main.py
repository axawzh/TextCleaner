from cleaner import Clean

output_path = './output/'
input_path = './input/'
text = open(input_path + 'demofile.txt', 'r', encoding='UTF-8').read()

cleaner = Clean()

text_cleaned = cleaner.clean(text, output_path, 'demodebug.txt', debug=1)
cleaner.checkcorrected(text_cleaned, output_path, 'checktruth.txt',)


output_file = open(output_path + 'demooutput.txt', 'w+')
output_file.write(text_cleaned)
output_file.close()
