import unittest
from src.main import countUniqueNames


class TestCountUniqueNames(unittest.TestCase):

    def test_single_name(self):
        result = countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")
        self.assertEqual(result, 1)

    def test_nicknames(self):
        result = countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli")
        self.assertEqual(result, 1)

    def test_typos(self):
        result = countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli")
        self.assertEqual(result, 1)

    def test_middle_name(self):
        result = countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah")
        self.assertEqual(result, 1)

    def test_diff_middle_name(self):
        result = countUniqueNames("Deborah S", "Egli", "Deborah J", "Egli", "Egli Deborah")
        self.assertEqual(result, 2)

    def test_last_name(self):
        result = countUniqueNames("Deborah", "Egli", "Deborah", "Michele", "Egli Deborah")
        self.assertEqual(result, 2)


    def test_multiple_names(self):
        result = countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli")
        self.assertEqual(result, 2)


    def test_empty_form(self):
        result = countUniqueNames("Michele", "Egli", "Deborah", "", "Michele Egli")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
