def linear_unsorted_array(array, value):
    # Iterate array
    for index in range(len(array)):
        # If value is found, return its index
        if array[index] == value:
            return index
        
    return None


def linear_sorted_search(array, value):
    # Iterate array
    for index in range(len(array)):
        # If value is found, return its index
        if array[index] == value:
            return index
        
        # If current array value is bigger than value, return None
        if array[index] > value:
            return None
        
    return None


# Binary search
def binary_search_recursive(array, value, start=None, end=None):
    # Prepare the variables this way, so the user can call
    # the function with just the array and value to be searched.
    # If start and none are not defined, the search is conducted
    # in the whole array.

    if start is None:
        start = 0

    if end is None:
        end = len(array) - 1

    midpoint = start + (end - start + 1 ) // 2
    #return midpoint

    # If the value is found in the midpoint, return its index
    if array[midpoint] == value:
        return midpoint
    
    # if the value being searched is smaller than the one in the midpoint
    # and there is at least one element left to the midpoint
    # - Perform the search on the left half
    if value < array[midpoint] and midpoint >= start+1:
        return binary_search_recursive(array, value, start=start, end=midpoint)
    
    # if the value being searched is bigger than the one in the midpoint
    # and there is at least one element right to the midpoint
    # - Perform the search on the right half
    if value > array[midpoint] and midpoint <= end-1:
        return binary_search_recursive(array, value, start=midpoint+1, end=end)
    
    return None



# print(binary_search_recursive([1, 2, 3, 4, 5, 6], 4))