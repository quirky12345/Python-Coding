from special_variable import add


def fun1():
    add()
    print("From fun1: ")


def fun2():
    print("From fun2: ")


def main():
    fun1()
    fun2()


if __name__ == "__main__":
    main()