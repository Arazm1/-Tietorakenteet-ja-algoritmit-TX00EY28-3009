from random import randint
import time


def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: The sorted array.
    """
    # If the array size is 1, just return the array
    if len(array) == 1:
        return array
    
    midpoint = len(array)//2
    
    """
    left_array = array[:midpoint]
    right_array = array[midpoint:]

    # recursion
    merge_sort(left_array)
    merge_sort(right_array)
    """
    left_array = merge_sort(array[:midpoint])
    right_array = merge_sort(array[midpoint:])

    # merge
    i = 0   # left_array idx
    j = 0   # right array idx
    k = 0   # merged array index
    merged = [0] * len(array)

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            merged[k] = left_array[i]
            i+=1
        else:
            merged[k] = right_array[j]
            j+=1
        k+=1
    
    while i < len(left_array):
        merged[k] = left_array[i]
        i+=1
        k+=1

    while j < len(right_array):
        merged[k] = right_array[j]
        j +=1
        k+=1
    
    return merged

"""
array = [6, 8, 5, 1, 2]
array2 = merge_sort(array)
print(array2)
"""

array=[randint(0,10000) for _ in range(10000)]
start_time = time.time()
_ = merge_sort(array)
runtime = time.time() - start_time
print(f'Merge sort runtime: {runtime}')