numbers = [93, 86, 11, 68, 70]
numbers.sort(reverse=True)
print(numbers)


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name}, {self.weight})'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

tools.sort(key=lambda x: x.weight)
print(tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('case sensitive: ', places)
places.sort(key=lambda x: x.lower())
print('case insensitive: ', places)

saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw)

drill = (4, 'drill')
sander = (4, 'sander')
assert drill < sander
