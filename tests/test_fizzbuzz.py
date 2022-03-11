from src.fizzbuzz import FizzBuzzEngine


def test_fizzbuzz_range_10():
    assert FizzBuzzEngine.fizzbuzz(10) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
    ]
