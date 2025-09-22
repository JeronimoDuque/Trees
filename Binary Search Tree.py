from Node_binary import Node_binary

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node_binary(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursively(self.root, new_node)

    def _insert_recursively(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.get_left() is None:
                current_node.add_left(new_node)
            else:
                self._insert_recursively(current_node.get_left(), new_node)
        else:
            if current_node.get_right() is None:
                current_node.add_right(new_node)
            else:
                self._insert_recursively(current_node.get_right(), new_node)

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursively(current_node.get_left(), value)
        else:
            return self._search_recursively(current_node.get_right(), value)

    def inorder_traversal(self):
        elements = []
        self._inorder_recursively(self.root, elements)
        return elements

    def _inorder_recursively(self, node, elements):
        if node is not None:
            self._inorder_recursively(node.get_left(), elements)
            elements.append(node.value)
            self._inorder_recursively(node.get_right(), elements)