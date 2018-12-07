def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
ret = avg(10)

ret1 = avg(11)

ret2 = avg(12)

print(ret, ret2, ret1)
