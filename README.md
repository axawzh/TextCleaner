# TextCleaner
Text Cleaner for raw text. 

pdf-client is required to download raw text from the pdf-server and post the output back.

To execute the cleaner with local text files, run `main.py`.

To execute the cleaner with server, set your server account in `config.json`, and run `postBook.py`.

config.json file is not included under this repo. Please use your own username and password in order to access the server.

The pdf-client is available [here](https://github.com/nathanielove/pdf-client).

The pdf-server is available [here](https://github.com/nathanielove/pdf-server).

## Input/Output files

There are two possible input sources: local files for testing and remote pdf-server.

To process text from remote pdf-server and then post it back, run `postBook.py`. In order to access the remote server, you must put your username and password in a `config.json` file, and put the file in root directory of the cleaner (parallel with main.py).

The format of `config.json`, change the url of the server, username and password accordingly:
```
{
  "base_url": "url_of_the_server",
  "auth_class": "HTTPBasicAuth",
  "auth_args": ["username", "password"]
}
```

Then in `postBook.py`, specify the location of the `config.json`.

In `postBook.py`, specify the source and target argument of `MultiThreadWorker` to specify the source target version. Detailed argument format of `MultiThreadWorker` can be found in [pdf-client repo](https://github.com/nathanielove/pdf-client).

To process text locally, run `main.py` with the files listed below.

### Local input
Put these files in the `input` folder for reading. Here the file names are default file names, you can use different names, but must update the file name in `main.py` accordingly.

`demofile.txt`: a sample input used for testing the functions of the cleaner.

`correcteddemotext.txt`: the ground truth manually obtained from the demofile.txt, used to check the correctness of the output of the cleaner.


### Local output
You can also customize the output file names in `main.py`. 

`demooutput.txt`: the output of the cleaner.

`checktruth.txt`: a file compares the code output with the ground truth in parallel.

`demodebug.txt`: shows the changes in input text during different stages of the pipeline, used to check if each stage functions correctly.


## `Clean` class in `cleaner.py`
###The `method` list
You can change the stages of the pipelines by modifying this list. 

Define your own stages in `cleaner.py` as a function, and add your function name into the list to add new pipeline stage.

Change the order of the function to change the order of the stages.

###The `clean` method 
This method is called in `main.py` to execute cleaner.

It takes 4 arguments:

| Parameter | Type | Explanation |
| --- | --- | --- | 
| txt | string | the raw text to be processed |
| path | string | the directory of the output |
| file_name | string | the name of the debug file |
| debug=[0,1] | int | pass 1 to enable output debug file |

It runs all the stages of the pipeline on the input text and returns the processed text.

###The `checksample` method
The method is called in `main.py` to create a file that compares the output of the cleaner with the manually edited ground truth in parallel.
It takes 4 arguments:

| Parameter | Type | Explanation |
| --- | --- | --- | 
| txt | string | the output text of the cleaner |
| path | string | the directory of the output and the ground truth |
| file_name_output | string | the name of the output |
| file_name_corrected | string | the name of the file contains the ground truth |

The output path is the same as the ground truth file, which is indicated by `path` argument.

###The `clean_server` method
This method is used together with pdf-client to process the text and post back to the server. This is implemented in `main.py` by the `CleanStart` class. In the pdf-client, the `postBook.py` class will be imported to execute the pipeline.

As only cleaned text files are to be post to the server. No auxiliary files should be generated such as debug file or check truth file. This is why the method does nothing other than running each stage on the input text.

## `check_english()` function in `cleaner.py`
This function is the most important stage of the pipeline. It is in charge of removing the formulas.

Specifically, the function tokenize the input text and try to check whether a token is a valid English vocabulary for all tokens. If yes, the token is joined back. Otherwise, a placeholder `[FORMULA]` or `[NUMERIC]` is joined back instead.

The dictionary is in form of a txt file. The directory of the dictionary is indicated at the beginning of the `cleaner.py`. User can use their own dictionary by modify the directory.

## `remove_bullet_pts()` and `remove_reference()` in `cleaner.py`
`remove_bullet_pts()` is in charge of remove bullet points and replace it with placeholder `[BULLET]`.

`remove_reference()` is in charge of remove IEEE style references in the text, and replace it with placeholder `[REF]`.

Both of them use regular expression to find their targets, so no tokenization is required.

## Placeholders in `cleaner.py`
The placeholders are defined at the beginning of the file. You can change the definition to use your own placeholder patterns instead of default ones.