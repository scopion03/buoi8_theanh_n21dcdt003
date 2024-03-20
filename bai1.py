class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    assert bst.root == None
    
    print("BinarySearchTree class and constructor are implemented successfully!")