import unittest
import valid


class Validations(unittest.TestCase):

    def test_validations_start0(self):
        # capture results of function
        result = valid.isValid("023-123-1234")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validations_11digits(self):
        # capture results of function
        result = valid.isValid("123-1234-1234")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validations_alphabet(self):
        # capture results of function
        result = valid.isValid("123123123a")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validation_start0_hasAlphabet(self):
        # capture results of function
        result = valid.isValid("021234r55")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validation_10digits(self):
        # capture results of function
        result = valid.isValid("9212349055")
        expected = "Matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validation_9digits(self):
        # capture results of function
        result = valid.isValid("023-13-1234")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validation_wrongformat(self):
        # capture results of function
        result = valid.isValid("(123)4567890")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validation_digitcount(self):
        # capture results of function
        result = valid.isValid("(123)-1234-1234")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_correctformat_withAlphabet(self):
        # capture results of function
        result = valid.isValid("(123)-1234-123a")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_wrongFormat2(self):
        # capture results of function
        result = valid.isValid("(123)-1234123")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validateCorrectFormat(self):
        # capture results of function
        result = valid.isValid("1231231234")
        expected = "Matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_wrongFormat3(self):
        # capture results of function
        result = valid.isValid("123-123-1234")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_allAlphabets(self):
        # capture results of function
        result = valid.isValid("qwertyuiop")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_correctForm(self):
        # capture results of function
        result = valid.isValid("(123)-123-1234")
        expected = "Matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_withSpecialChar(self):
        # capture results of function
        result = valid.isValid("123%$@#122")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)

    def test_validate_wrongPlaceHyphen(self):
        # capture results of function
        result = valid.isValid("(123)1-23-1234")
        expected = "Non-matching"
        # Check if captured result is same is expected result
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
