import unittest
from generate_equation import (
    handle_bracketless_string
)

class TestBracketless(unittest.TestCase):
    
    def test_can_handle_division(self):
        instr = 'x/y'
        expected_result = "x\n-\ny"

        result = handle_bracketless_string(instr)

        self.assertNotEqual(result, None)
        self.assertEqual(result, expected_result)
         
    def test_can_handle_normal_string(self):
        instr = 'x*y-z'

        result = handle_bracketless_string(instr)

        self.assertNotEqual(result, None)
        self.assertEqual(result, instr)
         
