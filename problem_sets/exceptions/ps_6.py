def invert_numbers(lst):
    try:
        inverse_lst = [1/float(n) for n in lst]
    except ZeroDivisionError as e:
        return f"Error: Cannot divide by zero - {e}"
    else:
        return inverse_lst

numbers = [1, 2, 0, 3, 4]
print(invert_numbers(numbers))