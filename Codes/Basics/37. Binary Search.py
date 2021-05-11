
pos = -1
def binary_search(list,n):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start+end)//2
        if list[mid] == n:
            globals()['pos'] = mid+1
            return True
        elif list[mid]>n:
            end = mid - 1
        else:
            start = mid + 1
    return False

list = [4,7,8,12,45,99]

n = 99

if binary_search(list, n):
    print("Found at: ", pos)
else:
    print("Not found")




list = [4,7,8,12,45,99]