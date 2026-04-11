class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
    def __repr__(self):
        return f'<ListNode: {self.data}>'
    


class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0


    def __repr__(self):
        current_node = self._head
        values = ''

        while current_node:
            values += f', {current_node.data}'
            current_node = current_node._next
        
        plural = '' if self._size == 1 else 's'
        return f'<SingleLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'
        
        #return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size


    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """

        # Create the node with the given value
        new_node = ListNode(value)

        # If list is empty, point the header and the tail pointers to the new node
        if self._tail is None:      # Or self._head is None
            self._head = self._tail = new_node
        
        else:
            # If not, update the last node and point it to the new node
            # and also update the tail pointer itself
            self._tail.next = new_node
            self._tail = new_node

        self._size +=1


    def pop(self):
        # List is empty
        if not self._head:
            return None
        
        # Only one Node
        if self._head.next is None:
            value = self._head.data
            # del self._head
            self._head = None
            return value


        # More than one Node
        current_node = self._head

        # Second last Node
        while current_node.next.next != None:
            current_node = current_node.next

        # Last node
        last_node = current_node.next
        data_value = last_node.data

        # Remove last node
        current_node.next = None

        return data_value



