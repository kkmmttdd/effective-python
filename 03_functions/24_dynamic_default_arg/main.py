from time import sleep
from datetime import datetime
import json


def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('Hi there!')
sleep(1.0)
log('Hi there!')


def decode(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad_data')
foo['stuff'] = 5
bar = decode('also_bad')
bar['meep'] = 1
print(f'foo: {foo}')
print(f'bar: {bar}')
