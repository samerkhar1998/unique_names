import unittest
from src.main import countUniqueNames


class TestCountUniqueNames(unittest.TestCase):

    def test_same_names(self):
        result = countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")
        self.assertEqual(result, 1)
    def test_nickname(self):
        result = countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli")
        self.assertEqual(result, 1)
    def test_typo(self):
        result = countUniqueNames("Deborah", "Egni", "Debbie", "Egli", "Egli Deborah")
        self.assertEqual(result, 1)
    def test_middle_name(self):
        result = countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah")
        self.assertEqual(result, 1)
    def test_diff_persons(self):
        result = countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli")
        self.assertEqual(result, 2)
    def test_diff_nickname_diff_persons(self):
        result = countUniqueNames("BOBBIE", "kharouba", "CLARA", "kharouba", "ROBERTA kharouba")
        self.assertEqual(result, 2)
    def test_diff_nickname_same_person(self):
        result = countUniqueNames("BOBBIE", "kharouba","BERTIE", "kharouba", "ROBERTA kharouba")
        self.assertEqual(result, 1)
    def test_diff_middle_name(self):
        result = countUniqueNames("Deborah S", "Egli", "Deborah J", "Egli", "Egli Deborah")
        self.assertEqual(result, 2)

    def test_empty_form(self):
        result = countUniqueNames("Michele", "Egli", "Deborah", "", "Michele Egli")
        self.assertEqual(result, -1)

    def test_not_string(self):
        result = countUniqueNames(5, "Egli", "Deborah", "Egli", "Michele Egli")
        self.assertEqual(result, -1)
    def test_bolean_input(self):
        result = countUniqueNames(True, "Egli", "Deborah", "Egli", "Michele Egli")
        self.assertEqual(result, -1)
    def test_string_with_numbers(self):
        result = countUniqueNames("Deborah 5", "Egli", "Deborah", "Egli", "Michele Egli")
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
