# node of a binary tree
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
Problem 1:
Given the root of a binary tree, conduct a pre-order traversal (current, left, 
right) and print each node in order.

E.g.

input:
        10
      /    \
     5      15
    / \    / \
   2   7  12   17

output:
10 5 2 7 15 12 17
"""
def pre_order(root):
    if not root:
        return
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)

"""
Problem 2:
Given the root of a binary tree, conduct an in-order traversal (left, current,
right) and print each node in order.

E.g.

input:
        10
      /    \
     5      15
    / \    / \
   2   7  12   17

output:
2 5 7 10 12 15 17
"""
def in_order(root):
   if not root:
        return
   in_order(root.left)
   print(root.data)
   in_order(root.right)

"""
Problem 3:
Given the root of a binary tree, conduct a post-order traversal (left, right,
current) and print each node in order.

E.g.

input:
        10
      /    \
     5      15
    / \    / \
   2   7  12   17

output:
2 7 5 12 17 15 10
"""
def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data) 

"""
Problem 4:
Given the root of a binary tree, find the number of nodes in the tree.

E.g.

input:
        10
      /    \
     5      15
    / \    / \
   2   7  12   17

output:
7
"""
def count_nodes(root):
     count = 1
     if root.left:
         count += count_nodes(root.left)
     if root.right:
         count += count_nodes(root.right)
     return count

def num_nodes(root):
    count = 0
    count += count_nodes(root)
    print(count)

"""
Problem 5:
Given the root of a binary tree, find its height. The height of the tree refers
to the length of the longest path between root and a leaf.

Tips:
For a null root, raise a TypeError; for a single node tree (just root) return
-1.

E.g.

input:
        10
      /    \
     5      15
    / \
   2   7

output:
2
"""

def get_height(root):
    if root.left and root.right:
        return 1 + max(get_height(root.left), get_height(root.right))
    elif root.left and (not root.right):
        return 1 + get_height(root.left)
    elif root.right and (not root.left):
        return 1 + get_height(root.right)
    else:
        return 1

def tree_height(root):
    if not root:
        raise TypeError("root cannot be null")
    if (not root.left) and (not root.right):
        return -1

    height = get_height(root) - 1
    print(height)

    return height

if __name__ == "__main__":
    # example tree
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right = Node(15)

    #pre_order(root)
    #in_order(root)
    #post_order(root)
    #num_nodes(root)
    tree_height(root)
