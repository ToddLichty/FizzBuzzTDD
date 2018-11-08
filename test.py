import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_TestNormalNumberReturned(self):
        
        self.assertEqual("1", fizzbuzz.fizzBuzzConvert(1))
        self.assertEqual("2", fizzbuzz.fizzBuzzConvert(2))

    def test_TestMultiplesOfThreeReturnFizz(self):
        self.assertEqual("Fizz", fizzbuzz.fizzBuzzConvert(3))
        self.assertEqual("Fizz", fizzbuzz.fizzBuzzConvert(21))
        self.assertEqual("Fizz", fizzbuzz.fizzBuzzConvert(99))

    def test_TestMultiplesOfFiveReturnBuzz(self):
        self.assertEqual("Buzz", fizzbuzz.fizzBuzzConvert(5))
        self.assertEqual("Buzz", fizzbuzz.fizzBuzzConvert(10))
        self.assertEqual("Buzz", fizzbuzz.fizzBuzzConvert(25))
        self.assertEqual("Buzz", fizzbuzz.fizzBuzzConvert(50))        

    def test_TestWithMultiplesOfBoth3And5(self):
        self.assertEqual("FizzBuzz", fizzbuzz.fizzBuzzConvert(15))
        self.assertEqual("FizzBuzz", fizzbuzz.fizzBuzzConvert(30))
