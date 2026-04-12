class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'
    

class HashTable():
    def __init__(self, size=20):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]>'
    

    def _hash(self, key):
        return len(key) % self.size
    

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """

        # Start to search from the given position
        current = start
        
        # While current position is occupied and it doesnt contain the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size     # esim. 0 + 1 % 20 = 1 % 20 = 0, 1 yli
            # If we reach again the given position, that means
            # a whole cycly has been completed and the key was not found
            if current == start:
                return None
            
        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None
        