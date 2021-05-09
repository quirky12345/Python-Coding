class Computer:
    # init is a constructor and it is called automatically everytime
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is: ",self.cpu,self.ram)

# initialize objects
comp1 = Computer('i5',16)
comp2 = Computer('Ryzen 3',8)

#another way of writing the same above thing
comp1.config()
comp2.config()

