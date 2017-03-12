# TextCleaner
Text Cleaner for raw text
config.json file is not included under this repo. Please use your own username and password in order to access the server.

## Input/Output files
demofile.txt: a sample input used for testing the functions of the cleaner.
demooutput.txt: the output of the cleaner.
correcteddemotext.txt: the ground truth manually processed from the demofile.txt, used to ckeck the correctness of the output of the cleaner.
checktruth.txt: a file compares the code output with the ground truth in parallel.
demodebug: shows the changes in input text during different stages of the pipeline, used to check if each stage functions correctly.

## `Clean` class
###The `method` list
You can change the stages of the pipelines here. 
Add function name into the list to add this function into the pipeline.
Change the order of the function to change the order of the stages.

###The `clean` method 
It takes 4 arguments:

| Parameter | Type | Explanation |
| --- | --- | --- | 
| txt | string | the raw text to be processed |
| path | string | the directory of the output |
| file_name | string | the name of the debug file |
| debug=[0,1] | int | pass 1 to use output debug file |

It runs all the stages of the pipeline on the input text and returns the processed text.

###The `checksample` method
The method creates a file that compares the output of the cleaner with the manually edited ground truth in parallel.
It takes 4 arguments:

| Parameter | Type | Explanation |
| --- | --- | --- | 
| txt | string | the output text of the cleaner |
| path | string | the directory of the output and the ground truth |
| file_name_output | string | the name of the output |
| file_name_corrected | string | the name of the file contains the ground truth |

The output path is the same as the ground truth file, which is indicated by `path` argument.

###The `clean_server` method
This method is used together with pdf-client to process the text and post back to the server. This is implemented in `main.py` by the `CleanStart` class. In the pdf-client, the `CleanStart` class will be imported to execute the pipeline.
As only cleaned text files are to be post to the server. No auxiliary files should be generated such as debug file or check truth file. This is why this method does nothing other than running each stage on the input text.




