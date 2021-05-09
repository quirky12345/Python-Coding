#filter takes two args - function and iterable which returns true or false
#Map takes two args - function and iterable. function can perform some operations
#reduce takes two args - function and sequence.
from functools import reduce
is_even = lambda n : n%2==0
nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(is_even,nums))
doubles = list(map(lambda n: n*2,evens))
sum = reduce(lambda a,b: a+b,doubles)
print(evens)
print(doubles)
print(sum)