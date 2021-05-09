class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

#  here class B is inhertiing class A, i.e. class B is child of class A.
# This is single level inheritance
class B(A):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

# This is multi level inheritance. C is inheriting from B, then from A as well.
class C(B):
    def feature5(self):
        print("Feature 5 is working")

b1 = C()
b1.feature1()