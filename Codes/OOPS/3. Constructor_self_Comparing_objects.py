class Computer:
    def __init__(self):
        self.name = "Chaitanya"
        self.age = 21

    def update(self):
        self.age = 30
    # compare(who is calling, whome to compare)
    def compare(self, other):
        return self.age == other.age


c1 = Computer()
c2 = Computer()
# self is c1 and other is c2
c1.update()
if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")
print(c1.age)
print(c2.name)