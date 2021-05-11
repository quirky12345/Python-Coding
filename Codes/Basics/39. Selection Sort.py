
def sort(nums):
    for i in range(len(nums)-1):
        for j in range(i, len(nums),1):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j],nums[i]

nums = [5, 3, 8, 6, 7, 2]

sort(nums)

print(nums)
