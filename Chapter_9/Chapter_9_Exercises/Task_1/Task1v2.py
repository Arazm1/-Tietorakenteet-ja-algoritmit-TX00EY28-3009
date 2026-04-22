# Example correct answer
# Not my solution

def insertion_sort(array):
    # The array will be traversed with a key_index
    for key_index in range(1, len(array)):
        # Store the value of key
        key = array[key_index]


        # Loop backwards through the sorted part of the
        # list (left of key_index) to find the correct
        # place for the key value

        back_index = key_index
        while back_index > 0 and array[back_index-1] > key:
            back_index -= 1

        # If back_index moved, then some elements have to be reordered
        if back_index < key_index:
            # Move elements to the right
            array[back_index+1:key+1] = array[back_index:key_index]
            # And insert the key at the position marked by the back_index
            array[back_index] = key
