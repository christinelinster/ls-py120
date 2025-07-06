def get_sixth(lst):
    if len(lst) < 6:
        return None
    return lst[5]

def get_sixth_afnp(lst):
    try:
        return lst[5]
    except IndexError:
        return None

numbers = [1, 2, 3, 4, 5]
print(get_sixth(numbers))
print(get_sixth_afnp(numbers))