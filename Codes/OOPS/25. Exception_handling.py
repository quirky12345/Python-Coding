# We will try to handle division by zero exception here

a = 5
b = 2
try:
    print("Resources Opened")
    print(a/b)
    print("I hope you have got your answer!")
    k = int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, you can't divide a number by zero")
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Something went wrong....")
# It doesn't matter if you are getting exception or not finally will run
finally:
    print("Resources Closed")