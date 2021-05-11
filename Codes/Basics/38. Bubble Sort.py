
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        swapped = False
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if swapped == False:
            return

nums = [3,2,1,7,5,6]

sort(nums)

print(nums)
