def interpolation_search(array, value):
    """
    Performs an Interpolation search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    start = 0
    array_size = len(array) -1
    end = array_size
    
    while value >= array[start] and value <= array[end] and start <= end:
        midpoint = start + int((end - start) * ((value-array[start])/(array[end]-array[start])))

        # print(f'midpoint: {midpoint}')

        if array[midpoint] == value:
            return midpoint
        elif array[midpoint] < value:
            start = midpoint+1
        else:
            end = midpoint-1

    return None



custom_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

interpolation_search(custom_array, 7)

