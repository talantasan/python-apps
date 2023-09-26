def fizz_buzz(x):
    if (x % 3 == 0) and (x % 5 == 0):
        result = "FizzBuzz"
    elif x  % 5 == 0:
        result = "Buzz"
    elif x % 3 == 0:
        result = "Fizz"
    else:
        result = x
    return result

print(fizz_buzz(3))