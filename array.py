from array import *

vals = array('i', [5, 2, 3])
# print(vals.buffer_info())
vals.reverse()
# copying vals for newArr
newArr = array(vals.typecode, (a for a in vals))
for i in newArr:
    print(i)