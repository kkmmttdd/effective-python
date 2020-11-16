from random import randint


def iterate_with_range():
    random_bits = 0
    for i in range(32):
        if randint(0, 1):
            # random_bits |= 1 << i
            random_bits |= 1 << i
    print(bin(random_bits))


def print_next(flavor_list):
    it = enumerate(flavor_list)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


def iterate_with_enumerate(flavor_list):
    for i, flavor in enumerate(flavor_list):
        print(f'{i} => {flavor}')


if __name__ == '__main__':
    iterate_with_range()
    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    print_next(flavor_list)
    iterate_with_enumerate(flavor_list)

