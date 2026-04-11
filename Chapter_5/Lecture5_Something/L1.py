class Node():
    def __init__(self, data, parent_node = None, left_child=None, right_child=None):
        self._data = data
        self._parent_node = parent_node
        self._left_child = left_child
        self._right_child = right_child


class Tree():
    def __init__(self):
        self._root_node = None

    
    def __insert__(self, data):

        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """

        # Let's use a couple of pointers to traverse the tree
        # following BST rules

        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node

            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node points to the node that should be the
        # Parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        # Link parent node the new Node

        # If tree is empty, just make the new node the root node
        if parent_node is None:
            self._root_node = new_node
            return
        
        # If value of new node is smaller than parent's, add new node to its left
        elif new_node.data < parent_node._data:
            parent_node._left_child = new_node
            # If value of new node is bigger than parent's, add new node to its right
        else:
            parent_node._right_child = new_node

        return

