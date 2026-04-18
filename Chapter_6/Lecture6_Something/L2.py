class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0
    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        # return len(key) % self.size
        return sum((index+1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.
        
        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Start to search from the given position
        current = start

        # While that position is in use, enter the loop
        while self.slots[current]:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            
            # If we reach again the given position, that means
            # a whole cycle has been completed and there was no free
            # positions available
            if current == start:
                return None

        # After the loop, current points to a free position
        return current

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupaid and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        # Raise an error if no space available
        if self.used_slots == self.size:
            raise(MemoryError('Hash table is full'))

        #  Try to find the key
        h = self._hash(key)
        q = self._find_key(h, key)
        if q is not None:
            # If found, update the value
            self.slots[q].value = value
        else:
            # If not found, find a free slot
            q = self._find_free_slot(h)
            # Add a new element.
            self.slots[q] = HashItem(key, value)
            # And increase used_slots
            self.used_slots += 1

    def get(self, key, alternative=None):
        """
        Get the value of 'key'.

        Parameters:
        - 'key': The key to find
        - 'alternative': An alternative value if key is not found. 
                         Optional. Default value=None
        
        Returns: The value of 'key' or alternative value
        """
        i = self._hash(key)
        existing_index = self._find_key(i, key)

        # Key exist, return value
        if existing_index is not None:
            value = self.slots[existing_index].value
            return 
        # Key doesnt exist, return alternative
        else:
            return alternative
        
    
    def remove(self, key):
        """
        Remove a key from the table

        Parameters:
        - 'key': key to remove

        Returns: None
        """

        # Find the position of given key
        freed_pos = self._find_key(self._hash(key), key)

        # If not found, return
        if freed_pos is None:
            return None
        
        # Define a helper lambda that gives the separation
        # in positions of a given position and the original
        # position a key should go
        separation = lambda pos, elem: (pos - self._hash(elem.key)) % self.size
        # Decrement the number of used slots
        self.used_slots -= 1


        while True:
            # Empty the position
            self.slots[freed_pos] = None
            # Prepare a helper pointer
            candidate_pos = freed_pos

            while True:
                # Move the helper pointer 1 position
                candidate_pos = (candidate_pos+1) % self.size
                # Save that positions content
                current_elem = self.slots[candidate_pos]
                # If position is empty, function can return
                if current_elem is None:
                    return
                
                # If the separation between current element's original position
                # and the position that was emptied is less than the separation
                # between the element's original position and the helper position
                # then exit the loop (to move the element to the emptied position)
                if separation(freed_pos, current_elem) < separation(candidate_pos, current_elem):
                    break
            
            # Move the element to the emptied position
            self.slots[freed_pos] = current_elem
            # New empty position is the helper position
            freed_pos = candidate_pos
