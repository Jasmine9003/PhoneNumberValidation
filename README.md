# PhoneNumberValidation
Verify if string is a phone number of valid format, 

#### Format1: (nnn)-nnn-nnnn
#### Format2: nnnnnnnnnn

Example: 
- (123) - 1234 - 1234 : Invalid 
- (123) - 1234 - 123a : Invalid
- 123 - 1234 - 1234 : Invalid
- 1231231234 : Valid
- 123123123a : Invalid
- (123)-123-1234: valid

## Requirements:
- Python 3.8.2 (used)
- PyCharm community version 
- Clone the github project
- pytest (pip install pytest) 
Note: Please Make sure that you install pytest in venv
- To use testrunner unittests, the file is <b>test_valid.py</b>: <b>COMMAND</b> -> python -m unittest test_valid.py
- To use testrunner pytest, the file is <b>test_valid1.py</b>: <b>COMMAND</b> -> pytest -v
- I have also added TestCase document (TestCaseDocument.xls) , giving details on the test cases verified.

### Project has 3 files: valid.py, test_valid.py and test_valid1.py
valid.py has the python code for checking if the string is of valid format, if yes, it is classified as Matching otherwise it is classified as Non-matching

I have tested this using 2 testrunners- unittests and pytest

- test_valid.py has the code using testrunner unittests
it can be run using the 'python -m unittest test_valid.py' inside venv

#### (venv) jasmine.dhunna@RWC-WS118 venv % python -m unittest test_valid.py
................
----------------------------------------------------------------------
Ran 16 tests in 0.001s

OK



#### test_valid1.py is used for testing the valid.py file and uses test runner pytest
- it imports pytest (to use this do : pip install pytest)
- It also imports valid (import valid) which is actually my valid.py file where my python code is present
- I have used pytest to test this script. 
- I have tested the script with different test cases and got the results in each of them. 
- Also committing a test case document for this script

### To run the script and test cases use: 

### pytest -v

Attaching the screenshot of the results.


<img width="1384" alt="Screen Shot 2020-05-07 at 3 45 18 PM" src="https://user-images.githubusercontent.com/25927257/81352846-6bf84a80-907c-11ea-90ce-14e036a8746d.png">
