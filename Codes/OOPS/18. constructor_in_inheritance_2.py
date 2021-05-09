class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        print("In B init")
    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In B init")
    def feature3(self):
        print("Feature 3 is working")

    def feat(self):
        super().feature1()


a1 = C()
a1.feat()