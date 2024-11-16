import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add_negative(self):
        self.assertEqual(self.calc.add(10,-30),-20)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(10,-30),40)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(10,-30),-300)
    def test_multiply_all_negative(self):
        self.assertEqual(self.calc.multiply(-10,-30),300)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
    def test_divide_negative_1(self):
        self.assertEqual(self.calc.divide(-30,10),-3)
    def test_divide_negative_2(self):
        self.assertEqual(self.calc.divide(31,-10),-3)
    def test_divide_all_negative(self):
        self.assertEqual(self.calc.divide(-53,-5),10)    
    def test_divide_by_0(self):
        self.assertEqual(self.calc.divide(100,0),"Error divider must not == 0")  

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
    def test_modulo_negative_1(self):
        self.assertEqual(self.calc.modulo(-47, 18),7)
    def test_modulo_negative_2(self):
        self.assertEqual(self.calc.modulo(78,-8),-2)
    def test_modulo_all_negative(self):
        self.assertEqual(self.calc.modulo(-50,-9),-5)    
    def test_modulo_by_0(self):
        self.assertEqual(self.calc.modulo(50,0),"Error divider must not == 0") 

if __name__ == '__main__':
    unittest.main()