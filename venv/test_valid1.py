import pytest
import valid


def test_validations_start0():
    # capture results of function
    result = valid.isValid("023-123-1234")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validations_11digits():
    # capture results of function
    result = valid.isValid("123-1234-1234")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validations_alphabet():
    # capture results of function
    result = valid.isValid("123123123a")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validation_start0_hasAlphabet():
    # capture results of function
    result = valid.isValid("021234r55")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validation_10digits():
    # capture results of function
    result = valid.isValid("9212349055")
    expected = "Matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validation_9digits():
    # capture results of function
    result = valid.isValid("023-13-1234")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validation_wrongformat():
    # capture results of function
    result = valid.isValid("(123)4567890")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validation_digitcount():
    # capture results of function
    result = valid.isValid("(123)-1234-1234")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_correctformat_withAlphabet():
    # capture results of function
    result = valid.isValid("(123)-1234-123a")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_wrongFormat2():
    # capture results of function
    result = valid.isValid("(123)-1234123")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validateCorrectFormat():
    # capture results of function
    result = valid.isValid("1231231234")
    expected = "Matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_wrongFormat3():
    # capture results of function
    result = valid.isValid("123-123-1234")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_allAlphabets():
    # capture results of function
    result = valid.isValid("qwertyuiop")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_correctForm():
    # capture results of function
    result = valid.isValid("(123)-123-1234")
    expected = "Matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_withSpecialChar():
    # capture results of function
    result = valid.isValid("123%$@#122")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected


def test_validate_wrongPlaceHyphen():
    # capture results of function
    result = valid.isValid("(123)1-23-1234")
    expected = "Non-matching"
    # Check if captured result is same is expected result
    assert result == expected
