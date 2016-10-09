from cleaner import Clean

output_path = './output/'
input_path = './input/'
text = open(input_path + 'demofile.txt', 'r').read()

cleaner = Clean()

text_cleaned = cleaner.clean(text, debug=1)

output_file = open(output_path + 'demooutput.txt', 'w+')
output_file.write(text_cleaned)
output_file.close()