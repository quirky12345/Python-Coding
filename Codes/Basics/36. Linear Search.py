
pos = -1
def search(list, n):
    # for i in list:
    #     if(i == n):
    #         globals()['pos'] = list.index(n)+1
    #         return True
    for i in range(len(list)):
        if (list[i] == n):
            globals()['pos'] = i+1
            return True

    return False

list = [5,8,4,6,9,2]
n = 9

if search(list,n):
    print("Found at ",pos)
else:
    print("Not Found")