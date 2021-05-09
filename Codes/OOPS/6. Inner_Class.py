class Student:
    def __init__(self,Name,RollNo):
        self.Name = Name
        self.RollNo = RollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.Name, self.RollNo," ",end="")
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Navin',2)
s2 = Student('Chaitanya',3)

s1.show()
s2.show()

