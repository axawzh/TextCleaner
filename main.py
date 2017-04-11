from cleaner import Clean

output_path = './output/'
input_path = './input/'

# Update the input file names here
input_filename = "demofile.txt"
input_checktruth_filename = 'correcteddemotext.txt'

# File names of the output files
output_filename = 'demooutput.txt'
output_debug_filename = 'demodebug.txt'
output_checktruth_filename = 'checktruth.txt'

# Open local file
text = open(input_path + input_filename, 'r', encoding='UTF-8').read()

cleaner = Clean() # Create cleaner

# Execute cleaner
text_cleaned = cleaner.clean(text, output_path, output_debug_filename, debug=1)
# Check truth
cleaner.checksample(text_cleaned, output_path, input_checktruth_filename, output_checktruth_filename)

# Output
output_file = open(output_path + output_filename, 'w+')
output_file.write(text_cleaned)
output_file.close()

# This class is invoked by postBook.py to execute cleaner
class CleanStart(object):
    cleaner = Clean()

    def run(self, text):
        text_cleaned = self.cleaner.clean_server(text)
        return text_cleaned
