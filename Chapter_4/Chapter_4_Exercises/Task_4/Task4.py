class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):    
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next

        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    
    def enqueue(self, data):

        # 1 - 2 - 3 - 4
        new_node = ListNode(data, next=None, prev=None)
        
        # if there's no existing Nodes
        # new_node becomes the head
        if not self._head:
            self._head = self._tail = new_node

        # If there is already existing Nodes
        else:
            # Only one Node
            if self._head == self._tail:
                old_head = self._head
                self._head = new_node

                new_node.next = old_head
                self._tail.prev = new_node
            
            # More than one Node
            else:
                old_head = self._head
                self._head = new_node

                new_node.next = old_head
                old_head.prev = new_node

        self._size += 1


    def dequeue(self):
        if not self._size:
            return None
        
        node_to_be_removed = self._tail
        
        # If head is same as tail
        if  self._head == self._tail:
            self._head = self._tail = None

        # If head is not same as tail
        else:
            second_last_node = self._tail.prev
            second_last_node.next = None
            self._tail = second_last_node

        self._size -= 1

        value = node_to_be_removed.data
        del(node_to_be_removed)
        return value

        


q = Queue()
print(q)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q)


""""

Implement a Node based Queue
You have to implement a Queue class called Queue 
that uses the ListNode class to store the data. 
ListNode class is already available.

Queue class should implement a __init__() method 
that initialize internal variables/properties. 
It also has to implement the enqueue and dequeue methods. 
These methods are very similar (if not the same) that some of the 
methods already available in the DoublyLinkedList class. 
So it can be of help to get these two methods. 
Finally a __repr__() method should be implemented. 
After enqueuing 'A', 'B' and 'C' (in this order), 
it should show a text like this:

<Queue (3 elements): [C, B, A]>

"""