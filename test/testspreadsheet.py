from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_integer_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_valid_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1","42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))

    def test_evaluate_formula_non_valid_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1","42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_non_valid_circular_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1","=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_arithmetic_formula_with_operator(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_arithmetic_formula_with_operator(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_divide_by_0_arithmetic_formula_with_operator(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_multiple_operators_arithmetic_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3*2")
        self.assertEqual(7, spreadsheet.evaluate("A1"))