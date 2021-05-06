# Break
# available = 20
# x = int(input("how much candies do you want? "))
# i = 1
# while i<=x:
#     if(i>available):
#         #print()
#         print("Sorry, we are out of Candies.")
#         break
#     print("Candy ",i," ")
#     i+=1

# Continue
# for i in range(1,101):
#     if i%3!=0:
#         continue;
#     print(i)

# Pass means there is no code, so move on

# for i in range(1,101):
#     if(i%2!=0):
#         pass
#     else:
#         print(i)

# Fibonacci

# def fibonacci(n):
#     if(n<0):
#         print("Wrong Input")
#     elif(n == 0):
#         return n
#     elif(n==1 or n==2):
#         return 1;
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(4))

# check prime
import math
n = int(input("Enter a number: "))
check = False
print(int(math.sqrt(n)))
for i in range(2,int(math.sqrt(n))):
    if(n%i==0):
        check = True
        break
if check:
    print("Number is not prime")
else :
    print("Number is prime")