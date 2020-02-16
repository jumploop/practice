import random


class BingoCage:
    first_name="firstname"
    last_name="lastname"
    def __init__(self, items, firstname, lastname):
        self._items = list(items)
        self.first_name = firstname
        self.last_name = lastname
        print(self._items)

        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()


upper_case_name.short_description = 'Customer name'
#
if __name__ == '__main__':
    print(upper_case_name.__dict__)
    bingo = BingoCage(range(10),"bob","smith")
    print(upper_case_name(bingo))
#     print(bingo.pick())
#     print(bingo())
