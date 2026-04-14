class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index-1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index-1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        current_index = 0

        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            smallest_index = current_index

            if left_child_index < self._size and self._heap[left_child_index] < self._heap[smallest_index]:
                smallest_index = left_child_index

            if right_child_index < self._size and self._heap[right_child_index] < self._heap[smallest_index]:
                smallest_index = right_child_index

            if smallest_index == current_index:
                break
            else:
                self._heap[current_index], self._heap[smallest_index] = self._heap[smallest_index], self._heap[current_index]
                current_index = smallest_index


    def _pop(self):
        index_of_root = 0
        index_of_last = self._size -1

        self._heap[index_of_root] = self._heap[index_of_last]
        # self._heap.pop(index_of_last)

        self._size -= 1


        


"""
h = Heap()
# h._heap = [3, 6, 5, 9, 7, 8, 4]
h._heap = [3, 5, 6, 9, 7, 8]
h._size = 6
print(h._heap)
h._float()
print(h._heap)

h._sink()
print(h._heap)

"""