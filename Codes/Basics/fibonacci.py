def fibonacci(n):
    if n < 0:
        print("Wrong number")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


result = fibonacci(5)
print(result)