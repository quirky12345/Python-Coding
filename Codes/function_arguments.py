#whenever you pass by value in python, python will pass it as pass by reference
#as you can see from the input to function below, id of x and a is same until you change the value of x
#as a result, there is no pass by value or pass by reference concept
def update(x):
    print(id(x))
    x = 8
    #integer are immutable in python, so as soon as you change the value
    #id/memory reference will change
    print(id(x))
    print(x)

a = 10
print(id(a))
update(a)
print(a)

#but if you pass list instead of integer it's id is going to remain same
#if you do any changes to any element of list in the function update
#because list is mutable
# def update(lst):
#     print(id(lst))
#     lst[0] = 8
#     print(id(lst))
#     print("x: ",lst)
#
# lst = [10,20,30,40]
# print(id(lst))
# update(lst)
# print("lst: ",lst)

