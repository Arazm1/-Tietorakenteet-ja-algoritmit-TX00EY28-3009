def bubble_sort(array):

    # Prepare a flag variable that will stop the main loop
    # if nothing has been done in that cycle
    # That means the array is already ordered the function
    # can stop.
    # The flag starts as True, so execution will enter the loop
    swapped = True
    # Prepare a pointer that will mark the limit between
    # the unsorted and sorted parts of the list.
    j = len(array)
    # Main loop
    while swapped:
        print('cycle')
        # Reset flag at the start of each cycle
        swapped = False
        # Traverse list from the start.
        # Elements already ordered (from j forwards) are not checked
        for i in range(0, j-1):
            # Swap if the current pair (i, i+1) is not sorted
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                #And rise up the variable flag
                swapped = True

        # In every cycle, one element is added to the sorted part of the list
        j -=1