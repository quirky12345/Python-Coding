# a = 10
# def something():
#     #local a
#     a = 15
#     print("inside func: ",a)
# something()
# print("Outside: ",a)

#if you want to use global a inside function

a = 10
def something():
    #using global a
    global a
    a = 15
    print("inside func: ",a)
something()
print("Outside: ",a)