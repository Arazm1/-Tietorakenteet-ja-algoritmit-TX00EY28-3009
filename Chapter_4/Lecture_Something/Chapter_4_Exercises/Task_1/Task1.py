class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """

        # YOUR CODE HERE. Remove the next line if necessary
        # return

        new_node = Node(data, next=None)

        if self._top is None:
            self._top = new_node

        else:
            old_top = self._top
            self._top = new_node
            new_node.next = old_top
        
        self._size += 1


    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """

        # YOUR CODE HERE. Remove the next line if necessary
        to_be_deleted = None

        if self._top is None:
            return None
        else:
            to_be_deleted = self._top
            # Theres only one Node
            if self._top.next is None:
                self._top = None
            # More than one Node
            else:
                new_top = self._top.next
                self._top = None
                self._top = new_top

            self._size -= 1
            return to_be_deleted.data



    def __repr__(self):
        # YOUR CODE HERE. Remove the next line if necessary
        values = ''
        current_node = self._top
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

