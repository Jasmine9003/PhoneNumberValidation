# PhoneNumberValidation
Verify if string is a phone number is of valid format

### Project has 2 files: valid.py, test_valid.py and test_valid1.py
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