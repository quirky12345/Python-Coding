#1. position arg

# def sum(a,b):
#     c = a+b
#     print(c)
#
# sum(5,4)

#2. keyword

# def name_age(name, age):
#     print(name," ",age)
#
# name_age(age = 27, name = "navin")

#3. default
#if age value is not passed, it will take 18 as default
# def name_age(name, age = 18):
#     print(name," ",age)
#
# name_age(name = "navin")

#4. variable, length
#here 4,6,78 will be assigned to b as a tuple
# def sum(a, *b):
#     c = a
#     for i in b:
#         c += i
#     print(c)
#
# sum(5,4,6,78)

#keyword variable length argument
#datatype of data sent is not same then use keywords, then again
#you have to use ** for sending data as argument
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i," ",j)
    # print(data)

person("Chaitanya",age = 21, city = "gangpur city",mobile = 9636020382)

