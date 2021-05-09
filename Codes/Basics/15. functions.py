def great():
    print("good morning!")
great()

# return addition of two numbers
def add(a,b):
    print(a+b)
add(3,4)

# return add and sub from one function
def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(4,3)
print(result1, result2)
