class Car:
    # Class/static variables are those who are define outside init
    # but inside class, and changes will affect all the objects
    wheels = 4
    # instance variables are those who are define inside init
    # and changes will not affect all the objects
    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
# wheels variable is shared with all the objects 
Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)