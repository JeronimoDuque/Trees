from Node import Node
class Node_binary(Node):
    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def is_leaf(self):
        return self.left is None and self.right is None 
    
