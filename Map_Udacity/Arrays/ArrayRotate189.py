#1st Solution
def rotate_arr(nums,k):
    nums[:] = nums[-k:] + nums[:-k]
    return nums

nums=[1,2,3,4,5,6,7]
k=3
print(rotate_arr(nums,k))

#2nd Solution:-
def rotate_arr(nums,k):
    arr= []
    arr[:]= nums[-k:]
    #print(arr)
    for i in range(-k,-1):
        nums.pop(i)
    nums.pop(-1)
    nums= arr + nums

    return nums
nums=[1,2,3,4,5,6,7]
k=3
print(rotate_arr(nums,k))
