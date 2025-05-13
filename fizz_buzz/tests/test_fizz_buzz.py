from src.fizz_buzz import fizz_buzz


def test_returns_number_when_not_multiple_of_3_or_5():
    assert fizz_buzz(1) == "1"


def test_returns_fizz_when_multiple_of_3():
    assert fizz_buzz(3) == "Fizz"


def test_returns_buzz_when_multiple_of_5():
    assert fizz_buzz(5) == "Buzz"


def test_returns_fizzbuzz_when_multiple_of_3_and_5():
    assert fizz_buzz(15) == "FizzBuzz"
