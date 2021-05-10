nums = [7,8,9,10]
# Defining iterator
it = iter(nums)
# first way of getting the value
print(it.__next__())
# second way of getting next value
print(next(it))

# desigining our own iterator
class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values = Topten()

# print(next(values))

for i in values:
    print(i)