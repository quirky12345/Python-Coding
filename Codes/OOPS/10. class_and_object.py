class Computer:
    def config(self):
        print("i5, 16GB, 1TB")
# initialize objects
comp1 = Computer()
comp2 = Computer()
# Calling function
Computer.config(comp1)
Computer.config(comp2)
#another way of writing the same above thing
comp1.config()
comp2.config()

a = 5
a.bit_length()