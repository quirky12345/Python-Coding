#abstract class and abstract method
#python does not directly directly support abstract classes and methods
#we have to import ABC class to make Computer class abstract
#Also, we can't create objects from abstract classes
#abstract method are those who has declaration but not definition/body

from abc import ABC,abstractmethod

class Computer(ABC):
    # decorator for abstract method
    @abstractmethod
    def process(self):
        pass

# Class Laptop will inherit abstract class Computer
# But we have to initialize all the abstract Methods of the abstract
# Class Computer to not get any error
class Laptop(Computer):
    def process(self):
        print("its running")

class whiteboard(Laptop):
    def write(self):
        print("its writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

com1 = Laptop()
com2 = whiteboard()
prog1 = Programmer()
prog1.work(com2)



