def even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2:
            odd += 1
        else:
            even += 1
    return even,odd

lst = [1,2,3,4,5]
even, odd = even_odd(lst)
print("even numbers: ", even)
print("odd numbers: ", odd)