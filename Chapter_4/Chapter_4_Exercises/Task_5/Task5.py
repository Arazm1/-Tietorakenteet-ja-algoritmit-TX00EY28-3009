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



# [2, 4, 3, 5, 6]
def get_pairs(list_of_num):
    even_queue = Queue()
    odd_queue = Queue()

    pairs = []

    for i in list_of_num:
        # Even
        if i % 2 == 0:
            # If Odd queue empty
            # Add number into Even queue
            if odd_queue._size == 0:
                even_queue.enqueue(i)
            
            # If odd queue is not empty
            # Make pairs
            else:
                num_to_remove = odd_queue.dequeue()
                # print(odd_queue)
                pairs.append((i, num_to_remove))

        # Odd
        if i % 2 != 0:
            # If Even queue is empty
            # Add number into Odd queue
            if even_queue._size == 0:
                odd_queue.enqueue(i)
            
            # If Even queue is not empty
            # Make pairs
            else:
                num_to_remove = even_queue.dequeue()
                # print(even_queue)
                pairs.append((num_to_remove, i))

    return pairs


get_pairs([2, 4, 3, 5, 6])

"""
q = Queue()
print(q)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
num = q.dequeue()
print(num)
print(q)
"""