def insertion_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, 0, -1):
             if nums[j-1] > nums[j] :
                 swap(nums, j, j-1)
                 j = j-1
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums), 1):
    #         if nums[i] > nums[j]:
    #             swap(nums, i, j)
    return nums

def swap(nums, i , j):
    temp= nums[i]
    nums[i] = nums[j]
    nums[j] = temp


nums = [55, -2, 34, 10, 0, 2, -5, 12]
print(insertion_sort(nums))