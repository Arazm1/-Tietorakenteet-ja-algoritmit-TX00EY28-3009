class ListNode():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'
    


class DoublyLinkedList:
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
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size
    

    def append(self, value):

        # Create the node with the value. This is the last node, so the next is None
        # but there can be already some other node in the list, hence the prev value
        new_node = ListNode(value, next=None, prev=self._tail)

        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # In any other case, update tail node to point to the new element
            # and update tail pointer. The new node already points to its
            # previous element
            self._tail.next = new_node # Take current last Node, and connect it to new last Node
            self._tail = new_node      # Mark the new Node as tail
        
        self._size += 1

    def pop(self):

        # List is empty, return None
        if not self._size:
            return None
        
        # Locate previous_node (second last Node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._head:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None

        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value








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



