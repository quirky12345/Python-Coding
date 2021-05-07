from array import *
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    arr = [0]*26
    check = False
    for j in range(0,len(s)):
        a = ord(s[j])-65
        if arr[a] == 0:
            arr[a]+=1
        else:
            if s[j-1] == s[j]:
                arr[a]+=1
            else:
                check = True
                break
    if check:
        print("NO")
    else:
        print("YES")