# def search(nums, key):
#     found = False
#     for i in range(len(nums)):
#         if nums[i]==key:
#             found = True
#     return found, key
#
#
# nums=[2,5,8,45,98]
# key= 58
# print(search(nums, key))

##------ Sorted array ------------------------------------
# def sortedlinearsearch(nums, key):
#     for i in range(len(nums)):
#         if nums[i] == key:
#             return True
#         if nums[i] > key:
#             return False
#     return False
#
# nums = [1,2,3,5,7,9]
# key = 10
# print(sortedlinearsearch(nums, key))

def linear_search(nums, key):
    found = False
    for i in range(len(nums)):
        if key == nums[i]:
            found = True
    return key, found

nums = [1,2,-8,-9,6,5]
key = -8
print(linear_search(nums, key))