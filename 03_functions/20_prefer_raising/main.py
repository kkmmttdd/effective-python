def careful_divide(a: float, b: float) -> float:
    """Divides by zero
    Raises:
        ValueError: When the inputs cannot be divided
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Input')


x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('invalid inputs')
else:
    print(f'result is {result}')
