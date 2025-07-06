
number = float(input("Choose a number: "))
if number < 0:
    raise ValueError("Negative numbers are not allowed!")
print(f"You entered {number}")