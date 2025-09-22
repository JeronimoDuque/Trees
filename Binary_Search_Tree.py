from Node_binary import Node_binary
from Binary_tree import Binary_tree

class BinarySearchTree(Binary_tree):
    def __init__(self):
        super().__init__()  # Llama al constructor de Binary_tree

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

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.add_left(self._delete_recursively(current_node.get_left(), value))
        elif value > current_node.value:
            current_node.add_right(self._delete_recursively(current_node.get_right(), value))
        else:
            # Caso 1: Sin hijos
            if current_node.get_left() is None and current_node.get_right() is None:
                return None
            # Caso 2: Un hijo
            if current_node.get_left() is None:
                return current_node.get_right()
            if current_node.get_right() is None:
                return current_node.get_left()
            # Caso 3: Dos hijos
            min_larger_node = self._find_min(current_node.get_right())
            current_node.value = min_larger_node.value
            current_node.add_right(self._delete_recursively(current_node.get_right(), min_larger_node.value))
        return current_node

    def _find_min(self, node):
        current = node
        while current.get_left() is not None:
            current = current.get_left()
        return current

