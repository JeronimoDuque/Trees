class Node:
    def __init__(self, data):
        self.data_value = data
        self.children_value = {}
        self.is_end = False

    @property
    def children(self):
        return self.children_value
    
    @children.setter
    def children(self, value):
        if not isinstance(value, Node) and not (isinstance(value, list) and all(isinstance(v, Node) for v in value)):
            raise TypeError("children must be a node or a list of nodes")
        self.children_value = value

    @property
    def data(self):
        return self.data_value
    
    @data.setter
    def data(self, value):
        self.data_value = value