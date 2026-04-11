## Write a method that detach a node from the tree

Given a basic BST structure (included), add a _detach_node() method to it, to search for values in the tree. The basic definition of the method is already included. The method accepts the node to be deleted as parameter and returns nothing.


The method should check on parent and possible children to change the connections and be sure that the tree remains functional after safely detaching the node from the tree. If the node to detach has two children, the method should raise a ValueError (it is not possible to just detach a node with two children from a BST). The method should also take into account when the node to detach is the root node.


Notice that the Node object, when printed, prints some odd code. This is done on purpose to help checking on the exercises.