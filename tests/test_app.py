import json
import unittest
from model import CASES, get_case, list_cases

class CaseTests(unittest.TestCase):
    def test_three_cases(self):
        self.assertEqual(len(list_cases()), 3)

    def test_case_fields(self):
        for cid in CASES:
            case = get_case(cid)
            for field in ('id', 'title', 'code', 'diagnosis', 'suggestion', 'evidence', 'verification', 'uncertainty'):
                self.assertIn(field, case)
            self.assertEqual(case['id'], cid)
            self.assertTrue(case['evidence'])

    def test_unknown_case(self):
        with self.assertRaises(ValueError):
            get_case('../other')

if __name__ == '__main__':
    unittest.main()
