def log(message, *args):
    if not args:
        print(message)
    else:
        values_str = ', '.join(str(v) for v in args)
        print(f'{message}: {values_str}')


log('My numbers are', 1, 2)
log('Hi there')
favorites = [11, 3, 4]
log('message', *favorites)
