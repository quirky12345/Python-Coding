def factorial(n):
    if n < 0:
        print("Wrong Value")
        return -1
    elif n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

result = factorial(5)
print(result)