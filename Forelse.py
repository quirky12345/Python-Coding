nums = [1,2,3,4,6]

#for else will work only with break,
for num in nums:
    if(num%5==0):
        print(num)
        break
#this below else is for "for" loop, but break is necessary
else:
    print("Not found")