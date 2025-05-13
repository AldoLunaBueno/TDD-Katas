def fizz_buzz(number: int):
    if number % 5 != 0 and number % 3 != 0:
        return str(number)
    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
