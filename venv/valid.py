import re


def isValid(s):

    pattern = re.compile("^\({1}[1-9][0-9]{2}\){1}-{1}[0-9]{3}-{1}[0-9]{4}$|^[1-9][0-9]{9}")

    if pattern.match(s):
        return "Matching"

    else:
        return "Non-matching"

