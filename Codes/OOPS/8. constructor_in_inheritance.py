class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

#  here class B is inhertiing class A, i.e. class B is child of class A.
# This is single level inheritance
class B(A):
    # If we don't define init in subclass then it will go and check superclass
    def __init__(self):
        # super is a constructor here
        # super representing super class
        # we are trying to access init of class A from class B
        super().__init__()
        print("In B init")
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a1 = B()