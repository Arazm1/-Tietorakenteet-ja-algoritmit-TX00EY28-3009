def heap_sort(array):
    # Create the heap
    h = Heap()
    # Insert the values on the heap
    for val in array:
        h.insert(val)

    # Return a sorted array, created by just popping the heap
    return [h.pop() for _ in range(len(array))]
    