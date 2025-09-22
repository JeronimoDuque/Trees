from Node import Node
class B_tree:
    def __init__(self, t):
        self.root = None
        self.t = t  # Minimum degree (defines the range for number of keys)