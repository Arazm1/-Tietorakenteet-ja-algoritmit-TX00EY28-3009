class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


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


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        
        if node._left_child is not None and node._right_child is not None:
            raise ValueError()
        
        else:
            if node._left_child is not None:
                child = node._left_child
            elif node._right_child is not None:
                child = node._right_child
            else:
                child = None


            # If it's a root node
            if node._parent is None:
                self._root_node = child
                if child is not None:
                    child._parent = None

            # If it's not a root node
            else:
                parent = node._parent

                # Check which side of the Parent the Node is attached to
                if parent._left_child == node:
                    parent._left_child = child
                else:
                    parent._right_child = child

                # Update the child's parent pointer if the child actually exists
                if child is not None:
                    child._parent = parent

    def _find_successor(self, node):
        """
        Find the successor of a node

        Parameters:
        - 'node': The node for whom a successor has to be found.
        
        Returns: Returns the succesor node or None if no successor is found.
        """

        current = node._right_child
        while current._left_child:
            current = current._left_child
        
        return current
    
    def _replace_node(self, node_to_replace, replacement_node):
        """"
        Link the parent and children of node to be replaced to the replacement node.
        Replacement node and node to be replaced must exist.
        Node to be replaced is not modified
        If node_to_replace is Root node, then _root_node pointer is updated.
        If BST rules are not fulfilled, an error is thrown.
        """

        # Check nodes exist.
        if node_to_replace is None or self.replace_node is None:
            raise(ValueError)
        
        parent_node = node_to_replace._parent

        #Link the replacement node to the parent
        replacement_node._parent = parent_node

        # If node to replace is Root node, update _root_node pointer.
        if node_to_replace is self._root_node:
            self._root_node = replacement_node

        # If not, link parent to the replacement on the right or the left
        # Replacement is left node
        if parent_node._left_child is node_to_replace:
            if replacement_node.data > parent_node.data:
                raise(ValueError)
            else:
                parent_node._left_child = replacement_node

        # Replacement is right node
        else:
            if replacement_node.data < parent_node.data:
                raise(ValueError)
            else:
                parent_node._right_child = replacement_node
        

        # Link replacement node to child nodes (if any)
        # From parent to child
        replacement_node._left_child = node_to_replace._left_child
        replacement_node._right_child = node_to_replace._right_child

        # From child to parent
        if replacement_node._left_child:
            if replacement_node._left_child.data > replacement_node.data:
                raise(ValueError)
            replacement_node._left_child._parent = replacement_node

        if replacement_node._right_child:
            if replacement_node._right_child.data < replacement_node.data:
                raise(ValueError)
            replacement_node._right_child._parent = replacement_node


    
    def remove(self, data):
        #Find the note to remove
        node_to_remove = self._find(data)
        #If node is not found, return
        if not node_to_remove:
            return
        
        # If node has only one or no child, just detach the node from the tree
        # Replacing it with one of its child (if any)
        if node_to_remove._left_child is None or node_to_remove._right_child is None:
            self._detach_node(node_to_remove)
        else:
            # Node to be removed has two children. Find its successor.
            # By definition the successor does not have a left child
            # (because then it would be the actual successor)
            successor_node = self._find_successor(node_to_remove)
            # Detach the successor from the tree
            self._detach_node(successor_node)
            # And replace the node to remove with the successor
            self._replace_node(node_to_remove, successor_node)


    def delete_node(self, data):
        node_to_remove = self._find(data)

        if node_to_remove is None:
            return


        if node_to_remove._left_child is None:
            self._shift_nodes(node_to_remove, node_to_remove._right_child)
        
        elif node_to_remove._right_child is None:
            self._shift_nodes(node_to_remove, node_to_remove._left_child)
        
        else:
            #y = self._find_successor(node_to_remove)
            y = node_to_remove._right_child
            while y._left_child is not None:
                y = y._left_child

            if y._parent != node_to_remove:
                self._shift_nodes(y, y._right_child)
                y._right_child = node_to_remove._right_child
                y._right_child._parent = y
            
            self._shift_nodes(node_to_remove, y)
            y._left_child = node_to_remove._left_child
            y._left_child._parent = y


    def _shift_nodes(self, u, v):
        if u._parent == None:
            self._root_node = v
        elif u == u._parent._left_child:
            u._parent._left_child = v
        else:
            u._parent_right_child = v
        
        if v != None:
            v._parent = u._parent


    def breadth_first_travelsal(self):
        values = []

        # Use a queue to store nodes to traverse
        queue = Queue()

        queue.enqueue(self._root_node)

        # Continue while there is a node in the queue
        while node := queue.dequeue():
            # Save the value of the node
            values.append(node.data)

            # Enqueue the left child
            if node._left_child:
                queue.enqueue(node._left_child)

            # Enqueue the right child
            if node._right_child:
                queue.enqueue(node._right_child)

        # Return values
        return values
    

    def depth_first_in_order(self, root_node=None, values=[]):
        """
        Traverse the tree in Depth-first in-order
        Parameters:
        - 'start_node': Optional. Where to start the traversal
        - 'values': Optional. A list of already visited nodes. For internal use only.
        Returns: A list of visited nodes in Depth-first in-order
        """
        # If no start node, start from the Root node
        if start_node is None:
            current = self._root_node
        else:
            current = start_node

        # Visit left child, if exists
        if current._left_child:
            self.depth_first_in_order(current._left_child, values)
        
        # Add current node value
        values.append(current.data)

        # Visit right child, if exists
        if current._right_child:
            self.depth_first_in_order(current._right_child, values)
        
        # Return list of visited nodes
        return values
    

    def depth_first_pre_order(self, root_node=None, values=[]):
        """
        Traverse the tree in Depth-first pre-order
        Parameters:
        - 'start_node': Optional. Where to start the traversal
        - 'values': Optional. A list of already visited nodes. For internal use only.
        Returns: A list of visited nodes in Depth-first pre-order
        """
        # If no start node, start from the Root node
        if start_node is None:
            current = self._root_node
        else:
            current = start_node

        # Add current node value
        values.append(current.data)

        # Visit left child, if exists
        if current._left_child:
            self.depth_first_pre_order(current._left_child, values)
        
        # Visit right child, if exists
        if current._right_child:
            self.depth_first_pre_order(current._right_child, values)
        
        # Return list of visited nodes
        return values
    

    def depth_first_post_order(self, root_node=None, values=[]):
        """
        Traverse the tree in Depth-first post-order
        Parameters:
        - 'start_node': Optional. Where to start the traversal
        - 'values': Optional. A list of already visited nodes. For internal use only.
        Returns: A list of visited nodes in Depth-first post-order
        """
        # If no start node, start from the Root node
        if start_node is None:
            current = self._root_node
        else:
            current = start_node

        # Visit left child, if exists
        if current._left_child:
            self.depth_first_post_order(current._left_child, values)
        
        # Visit right child, if exists
        if current._right_child:
            self.depth_first_post_order(current._right_child, values)
        
        # Add current node value
        values.append(current.data)
        
        # Return list of visited nodes
        return values



