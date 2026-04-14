class Heap():
    def __init__(self):
        self._heap = []
        self._size = 0


    def _float(self):
        index = self._size -1
        while index > 0:
            parent_index = (index-1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]

                index = parent_index

    
    def _insert(self, value):
        self._heap.append(value)
        self._float()
        self._size += 1