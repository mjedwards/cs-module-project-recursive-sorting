# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    merge_arr = []
    i, x = 0, 0
    # Your code here
    while len(merge_arr) < elements:
        if arrA[i] < arrB[x]:
            merge_arr.append(arrA[i])
            i+=1
        else:
            merge_arr.append(arrB[i])
            i+=1
        
        if i == len(arrA) or x == len(arrB):
            merge_arr.extend(arrA[i:] or arrB[x:])

    return merge_arr

# TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):
#     # Your code here
#     if len(arr) < 2:
#         return arr
#     mid_point = len(arr) // 2
#     left_side = arr[:mid_point]
#     right_side = arr[mid_point:]


#     return merge(left_side, right_side)
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid_point = len(arr) // 2
        left_side = arr[:mid_point]
        right_side = arr[mid_point:]
        left_side = merge_sort(left_side)
        right_side = merge_sort(right_side)

        arr = []

        while len(left_side) > 0 and len(right_side) > 0:
            if left_side[0] < right_side[0]:
                arr.append(left_side[0])
                left_side.pop(0)
            else:
                arr.append(right_side[0])
                right_side.pop(0)
        
        for i in left_side:
            arr.append(i)

        for i in right_side:
            arr.append(i)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

