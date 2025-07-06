
try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = num1 / num2
except ZeroDivisionError as e:
    print("Cannot divide by zero.")
    print("ZeroDivisionError: ", e)

except ValueError as e:
    print("Please provide a valid number.")
    print("ValueError:", e)
else:
    print(f"The result is: {result}")
finally:
    print("End of the program")
