def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    start = 0
    array_size = len(array) - 1
    end = array_size
    
    midpoint = start + (end - start +1) // 2

    if array[midpoint] == value:
        return midpoint
    
    # Value < midpoint value
    # current index midpoint(-1 every loop) and its higher than start(0) index
    if value < array[midpoint] and midpoint >= start +1:
        current_index = midpoint
        while value != array[current_index] and array[current_index] > array[start]:
            current_index-= 1
            if value == array[current_index]:
                return current_index

    # Value > midpoint value
    # current index midpoint(+1 every loop) and its lower than end index
    if value > array[midpoint] and midpoint <= end-1:
        current_index = midpoint-1
        while value != array[current_index] and array[current_index] < array[end]:
            current_index +=1
            if value == array[current_index]:
                return current_index
        
    return None
    

# print(binary_search_iterative([1, 2, 3, 4, 5], 5))