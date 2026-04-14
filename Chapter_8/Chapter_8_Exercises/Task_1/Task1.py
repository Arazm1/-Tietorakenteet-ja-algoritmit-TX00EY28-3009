class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        # Start with the index of the last element
        current_index = len(self._heap) -1


        while current_index > 0:
            parent_index = (current_index-1) // 2

            # If the child (current_index) is smaller than parent, swap
            if self._heap[current_index] < self._heap[parent_index]:
                
                self._heap[current_index], self._heap[parent_index] = self._heap[parent_index], self._heap[current_index]

                current_index = parent_index

            else:
                break


	
h = Heap()
h._heap = [3, 6, 5, 9, 7, 8, 4]
h._size = 7
print(h._heap)
h._float()
print(h._heap)