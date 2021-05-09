# print(__name__)

def add():
    print("a and b is added: ", __name__)

def sub():
    print("a and b is subtracted: ")

def main():
    add()
    sub()

if __name__ == "__main__":
    main()