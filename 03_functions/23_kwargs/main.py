def print_parameters(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} = {v}')


print_parameters(alpha=1, beta=0.1, gamma=0.4)
