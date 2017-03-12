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


