
def fizzBuzzConvert(numberToConvert):

    if numberToConvert % 15 == 0:
        return "FizzBuzz"

    if numberToConvert % 3 == 0:
        return "Fizz"

    if numberToConvert % 5 == 0:
        return "Buzz"
    
    return str(numberToConvert)