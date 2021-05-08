def even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2:
            odd += 1
        else:
            even += 1
    return even, odd
n = int(input("Enter the size of list: "))
lst = []
for i in range(n):
    a = int(input("Enter the number: "))
    lst.append(a)
even, odd = even_odd(lst)
print("even numbers: ", even)
print("odd numbers: ", odd)
print("Even : {} and Odd: {}".format(even,odd))