import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))
ret = bingo.pick()
print(ret)
print(bingo())
print(callable(bingo))