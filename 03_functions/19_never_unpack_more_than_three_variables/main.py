def get_status(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_status(lengths)
print(f'Min: {minimum}, Max: {maximum}')

first, second = 1, 2


def my_function():
    return 1, 2


first, second = my_function()


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')


assert first == 1
assert second == 2
