def is_triangle(sides):
    """
    Validates if the input sides can form a triangle.
    :param sides: A list or tuple of three positive numbers.
    :return: True if the sides form a triangle, False otherwise.
    """
    if not isinstance(sides, (list, tuple)) or len(sides) != 3:
        return False
    a, b, c = sides
    if any(type(x) not in (int, float) or x <= 0 for x in (a, b, c)):
        return False
    return a + b > c and a + c > b and b + c > a


print(is_triangle([3, 4, 5]))  # True
print(is_triangle([1, 2, 3]))  # False
print(is_triangle([5, 12, 13]))  # True
print(is_triangle([1, 1, 2]))  # False