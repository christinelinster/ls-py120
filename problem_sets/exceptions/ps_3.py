
try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = num1 / num2
except (ZeroDivisionError, ValueError) as e:
    print("Error: ", e)

else:
    print(f"The result is: {result}")
finally:
    print("End of the program")
