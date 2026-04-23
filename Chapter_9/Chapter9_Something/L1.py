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




def selection_sort(array):
    # Traverse the array
    for main_index in range(0, len(array) - 1):
        # On each cycle, minimum index is set to current index
        min_index = main_index
        # Search the rest of the array for a value smaller than
        # the one at min_index. If found, update min_index to point to it
        for search_index in range(main_index+1, len(array)):
            if array[search_index] < array[min_index]:
                min_index = search_index
        
        # If the index of the minimum value is different than the index
        # of the current value, then swap them.
        if min_index != main_index:
            array[min_index], array[main_index] = array[main_index], array[min_index]




def quick_sort(array, left_index=None, right_index=None):
    # Set these values fo the function can be called by the user with only the array
    # as parameter
    if not left_index:
        left_index = 0
    
    if not right_index:
        right_index = len(array) -1

    # The pivot selection is a problem in its own
    # For now let's use the first element, but any other element could have
    # been chosen (with necessary algorithm's adjustments)
    pivot_index = left_index

    # We set a border index to indicate that values less or equal
    # than pivot are to its left (border index inclusive) and values
    # bigger than pivot are at its right
    # Right now th eonly element less or equal than the pivot, is the
    # pivot itself.
    border_index = left_index

    # And start traversing the partition
    for current in range(left_index+1, right_index+1):
        # If the value of the current position is less than pivot,
        # Lets add it (current value) to the minors part
        if array[current] <= array[pivot_index]:
            # Update border as there is one minor more now.
            border_index +=1
            # Check if we actually need to do the swap. If current index was
            # the next value after minors, then no swap is necessary
            if current > border_index:
                # If that was not the case, then swap their values
                array[current], array[border_index] = array[border_index], array[current]

    
    # After traversing the partition, the pivot can be swapped with the last of the minors.
    # If pivot is the only minor, then there is no need to swap.
    if border_index != pivot_index:
        # swap
        array[border_index], array[pivot_index] = array[pivot_index], array[border_index]
        pivot_index = border_index # Update pivot index after swap

    # The pivot is in its position and all values less or equal than pivot are at the left,
    # and all values bigger than pivot are at the right.
    # Now call recursively this function on both partitions.
    # Check if the left partition has at least 2 elements
    if(pivot_index - left_index) > 1:
        quick_sort(array, left_index, pivot_index-1)
    # Check if the right partition has at least 2 elements
    quick_sort(array, pivot_index+1, right_index)