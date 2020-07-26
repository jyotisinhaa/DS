# def binarysearch(arr, key):
#     found = False
#     low = 0
#     high = len(arr)-1
#     while low <=high and not found:
#         mid = (low + high) // 2
#         if arr[mid]== key:
#             found = True
#         elif key > arr[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     if found == True:
#         print('Key is found')
#     else:
#         print('Key is not found')
#
# arr = [2,5,9,18,20]
# key = 21
# print(binarysearch(arr, key))

###--------------Amulus Academy------------------
def binary_search(nums, key):
    found = False
    low = nums[0]
    high = nums[len(nums) - 1]
    while low > high and not found:
        mid = (low + high) // 2
        if nums[mid] == key:
            found = True
            print("key found")
        elif nums[mid] < key:
            low = mid -1
        else:
            high = mid +1
    if found == True:
         print("key is found")
    else:
         print("Key not found")


nums = [2,5,9,18,20]
key = 6
print(binary_search(nums, key))