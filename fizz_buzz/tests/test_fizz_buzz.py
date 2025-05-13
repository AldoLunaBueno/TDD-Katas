from src.fizz_buzz import fizz_buzz


def test_returns_number_when_not_multiple_of_3_or_5():
    assert fizz_buzz(1) == "1"
