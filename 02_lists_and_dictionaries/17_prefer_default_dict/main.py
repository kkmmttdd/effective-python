from collections import defaultdict

visits = {
    'Mexico': {'Tulum': 'Puerto Vallarta'},
    'Japan': {'Hakone'}
}

visits.setdefault('France', set()).add('Arles')
visits.setdefault('Japan', set()).add('Arles')

print(visits)


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
print(visits.data)
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data)
print(visits.data.get('England'))
