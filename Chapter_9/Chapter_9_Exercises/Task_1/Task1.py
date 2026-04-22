def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    indexing_length = range(1, len(array))

    for i in indexing_length:
        value_to_sort = array[i]

        while array[i -1] > value_to_sort and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i = i-1

    return array
        