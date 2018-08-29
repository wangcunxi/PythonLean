from Array import *

ARRAY_SIZE = 10

array = Array(ARRAY_SIZE)
for i in range(array.len()):
    array.setitem(i,i*2)

for i in range(array.len()):
    value = array.getitem(i)
    if value == i* 2:
        print(value),
    else:
        print("Error on index %d, the error value is %d" % (i,value))
