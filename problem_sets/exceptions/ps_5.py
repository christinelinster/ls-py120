class NegativeNumberError(ValueError):
    pass

number = float(input("Choose a number: "))
if number < 0:
    raise NegativeNumberError("Negative numbers are not allowed!")
print(f"You entered {number}")

