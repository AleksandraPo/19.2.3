import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def tests_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2, 2) == 4

    def tests_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def tests_division_calculate_correctly(self):
        assert self.calc.division(self,2, 2) == 1

    def tests_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self,2, 2) == 0

    def tests_addin_calculate_correctly(self):
        assert self.calc.addin(self,2, 2) == 4

