# node of a binary search tree
class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

"""
Problem 1:
Given the root of a binary search tree, determine if a node with the specified
key exists.

E.g.
input: key=5

        (10: "Udon")
          /      \
   (5: "Bun")   (15: "Toaster")

output: True
"""
def exists(root, key):
    if not root:
        return False
    if key == root.key:
        return True
    
    if key > root.key:
        return exists(root.right, key)
    elif key < root.key:
        return exists(root.left, key)
"""
Problem 2:
Given the root of a binary search tree and a key return the corresponding value
if it exists, else raise a KeyError.

E.g.
input: key=5

        (10: "Udon")
          /      \
   (5: "Bun")   (15: "Toaster")

output: "Bun"
"""
def find(root, key):
    if not root:
        raise KeyError("key does not exist.")
    if key == root.key:
        return root.val

    if key > root.key:
        return find(root.right, key)
    elif key < root.key:
        return find(root.left, key)

"""
Problem 3:
Given the root of a binary search tree, insert the specified (key: value) pair,
or overwrite if a node with that key exists already. Return the (possibly new)
root of the updated tree

E.g.
input: (7: "Sexy Burger")
        (10: "Udon")
          /      \
   (5: "Bun")   (15: "Toaster")

output: (inserted Sexy Burger)
        (10: "Udon")
          /      \
   (5: "Bun")   (15: "Toaster")
          \
        (7: "Sexy Burger")
"""

def insert(root, key, val):
    if not root:
        return Node(key, val)

    if key < root.key: 
        root.left = insert(root.left, key, val)
    elif key > root.key:
        root.right = insert(root.right, key, val)
    elif key == root.key:
        root.val = val
    
    return root


"""
Problem 4:
Given the root of a binary search tree, delete the node with the specified
key. Raise a KeyError if it DNE. Return the (possibly new) root of the updated
tree.

E.g.
input: key=5
        (10: "Udon")
          /      \
   (5: "Bun")   (15: "Toaster")
          \
        (7: "Sexy Burger")

output: (deleted Bun)
                (10: "Udon")
                  /      \
   (7: "Sexy Burger")   (15: "Toaster")

Three cases when removing node k:

    1. k is a leaf node: remove directly
    2. k has one child: update root k with child's (key, val)
    3. k has two children:
        (1) replace root k with in-order successor, i.e. min key in right
            tree (or max key in left tree)
        (2) remove the in-order successor node from sub tree
"""

# consider right tree only
# this is to find the left-most node in tree

def find_min_successor(root):
    cur = root
    while cur.left:
        cur = cur.left

    return cur

def remove(root, key):
    if not root: 
        return root
        
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # otherwise if root has 2 children:
        temp = find_min_successor(root.right)
        
        # replace root with temp
        root.key = temp.key
        root.val = temp.val
        
        # remove temp from subtree
        root.right = remove(root.right, temp.key)
    
    return root
        
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    # example binary search tree
    root = Node(10, "Udon")
    root.left = Node(5, "Bun")
    root.left.left = Node(2, "Xiong Xiong")
    root.left.right = Node(7, "Sexy Burger")
    root.right = Node(15, "Toaster")

    #print(exists(root, 7))
    #print(exists(root, 20))
    #print(exists(root, 1))
    #print(exists(root, 6))

    #print(find(root, 15))
    #print(find(root, 8))

    #preorder(insert(root, 4, "weng"))
    
    preorder(remove(root, 10))
