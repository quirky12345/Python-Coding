
# f is just a reference
# our interntion is to read
f = open('Mydata.txt','r')

# read will help in printing whole file
print(f.read())
# read line will have a pointer to first line and it will print it
print(f.readline(),end="")
print(f.readline())

# our intention is to write now
# in write command, it will check if Newline.txt is there or not
# if not, it will create a new text file with name Newline.txt
# in mode 'w', everytime you write something, it will erase all the
# text you written earlier on the file and append what you are giving right nor
# So, for append in file we will use mode 'a'


f1 = open('Newline.txt', 'w')
# f1 = open('Newline.txt', 'a')
f1.write("This is my time. Bloody right here, right now")

#Now we will try to read all the data from Mydata and copy paste it to Newline.txt

for data in f:
    f1.write(data)
