from src.fizzbuzz import FizzBuzzConverter


def testConvert1ShouldBe1():
    assert FizzBuzzConverter.convert(1) == "1"

def testConvert3ShouldBeFizz():
	assert FizzBuzzConverter.convert(3) == "Fizz"

def testConvert5ShouldBeBuzz():
	assert FizzBuzzConverter.convert(5) == "Buzz"

def testConvert9ShouldBeFizzBuzz():
	assert FizzBuzzConverter.convert(9) == "Fizz"

def testConvert4ShouldBeFizzBuzz():
	assert FizzBuzzConverter.convert(4) == "4"

def testConvert15ShouldBeFizzBuzz():
	assert FizzBuzzConverter.convert(15) == "FizzBuzz"

def testConvert30ShouldBeFizzBuzz():
	assert FizzBuzzConverter.convert(30) == "FizzBuzz"
