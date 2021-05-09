# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = 5
b = 6
# temp = a
# a = b
# b = temp
# a = a+b #we are wasting one bit here
# b = a-b
# a = a-b

#we are not wasting one here below
# a = a ^ b
# b = a ^ b
# a = a ^ b

#python best practice for swap variable
#value of a and value of b goes into stack and it will reverse
#rot_two() in python
a,b = b,a
print(a)
print(b)

