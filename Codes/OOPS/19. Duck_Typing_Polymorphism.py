class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

# ide = PyCharm()
ide = MyEditor()
Laptop1 = Laptop()
Laptop1.code(ide)