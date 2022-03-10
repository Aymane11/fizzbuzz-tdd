from src.fizzbuzz import FizzBuzzConverter


def testConvert1ShouldBe1():
    assert FizzBuzzConverter.convert(1) == "1"

def testConvert3ShouldBeFizz():
	assert FizzBuzzConverter.convert(3) == "Fizz"

def testConvert5ShouldBeBuzz():
	assert FizzBuzzConverter.convert(5) == "Buzz"
