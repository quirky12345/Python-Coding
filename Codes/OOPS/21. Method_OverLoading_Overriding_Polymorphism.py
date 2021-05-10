# Method Overloading
# python doesn't directly support method overloading

class Student:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None :
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        elif a!=None:
            s = a
        return s

s1 = Student()
print(s1.sum(5, 9, 4))

# Method Overriding
# E.g. - My phone overrides my father phone

class A:
    def show(self):
        print("In A show func")

class B(A):
    # this show function overrides A's show function
    def show(self):
        print("In B show")

a1 = B()
a1.show()