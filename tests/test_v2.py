import os
import unittest
from unittest.mock import patch
from app import validate_analysis
from model import static_check, diagnose

class V2Tests(unittest.TestCase):
    def test_static_check_no_execution(self):
        result = static_check("raise RuntimeError('should not run')")
        self.assertEqual(result['status'], 'syntax_ok')
    def test_syntax_error(self):
        self.assertEqual(static_check('def x(:')['status'], 'syntax_error')
    def test_input_validation(self):
        self.assertEqual(validate_analysis({'code':'print(1)', 'expected':'1', 'observed':'0'})[0], 'print(1)')
        with self.assertRaises(ValueError):
            validate_analysis({'code':''})
    def test_missing_provider_config(self):
        with patch.dict(os.environ, {'DEBUGVERIFY_API_KEY':'','DEBUGVERIFY_MODEL':'','DEBUGVERIFY_API_URL':''}):
            with self.assertRaisesRegex(ValueError, 'not configured'):
                diagnose('print(1)', '1', '0')

if __name__ == '__main__':
    unittest.main()
