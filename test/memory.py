import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv=memoryview(numbers)
l=len(memv)
print(l)
print(memv[0])

memv_oct=memv.cast('B')
mlist=memv_oct.tolist()
print(mlist)
memv_oct[5]=4
print(numbers)