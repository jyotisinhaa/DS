def selection_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums), 1):
            if nums[i] > nums[j]:
                swap(nums, i, j)
    return nums

def swap(nums, i, j):
    temp= nums[i]
    nums[i] = nums[j]
    nums[j] = temp

nums = [9, 8,7,6,5,2,1,0,-3,-9,-19]
print(selection_sort(nums))
##--complexity is O(n2)