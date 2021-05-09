class Student:
    # Class/Static variables
    school = 'Telusko'
    def __init__(self,m1,m2,m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # example of instance methods - Instance methods are related to Instance variables
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3.0

    # Getters(Accessor Methods) - Comes under instance Methods
    def get_m1(self):
        return self.m1

    def get_m2(self):
        return self.m2

    def get_m3(self):
        return self.m3

    # Settors(Mutator methods) - Comes under instance Methods
    def set_m1(self,value):
        self.m1 = value

    def set_m2(self,value):
        self.m2 = value

    def set_m3(self,value):
        self.m3 = value

    # Class methods below is related to class variables
    @classmethod
    def get_school(cls):
        return cls.school
    # Static Method is not related to any variables
    @staticmethod
    def info():
        print("This is Student Class. Also, this is static method")


s1 = Student(63,45,78)
s2 = Student(89,32,93)

print(s1.avg())
print(Student.get_school())
Student.info()


