import functools


def deco(func):
    @functools.wraps(func)
    def inner():
        print('running inner()')
        func()
    return inner

@deco
def target():
    print('running target()')

target()
print(target.__name__)