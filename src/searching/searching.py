# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # print(end)
    # Your code here
    if end >= start:
        mid_point = (end + start) // 2
        # print(mid_point)
        # print(mid_point - 1)
        # print(mid_point + 1)
        if arr[mid_point] == target:
            return mid_point 
        elif arr[mid_point] > target:
            return binary_search(arr, target, mid_point - 1, start)
        else:
            return binary_search(arr, target, mid_point + 1, end)
    else:
        return -1  # not found

arr1  = [1,2,4,6,9,10,23]
print(binary_search(arr1, 10, 0, len(arr1)-1))
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

