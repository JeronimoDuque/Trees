from Node_binary import Node_binary
from Binary_tree import Binary_tree
class AVLTree(Binary_tree):
    def __init__(self):
        super().__init__()  # Llama al constructor de Binary_tree

    def insert(self, value):
        new_node = Node_binary(value)
        if self.root is None:
            self.root = new_node
        else:
            self.root = self._insert_recursively(self.root, new_node)

    def _insert_recursively(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.get_left() is None:
                current_node.add_left(new_node)
            else:
                current_node.add_left(self._insert_recursively(current_node.get_left(), new_node))
        else:
            if current_node.get_right() is None:
                current_node.add_right(new_node)
            else:
                current_node.add_right(self._insert_recursively(current_node.get_right(), new_node))

        # Update the height of the ancestor node
        current_node.height = 1 + max(self._get_height(current_node.get_left()), self._get_height(current_node.get_right()))

        # Get the balance factor
        balance = self._get_balance(current_node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and new_node.value < current_node.get_left().value:
            return self._right_rotate(current_node)

        # Right Right Case
        if balance < -1 and new_node.value > current_node.get_right().value:
            return self._left_rotate(current_node)

        # Left Right Case
        if balance > 1 and new_node.value > current_node.get_left().value:
            current_node.add_left(self._left_rotate(current_node.get_left()))
            return self._right_rotate(current_node)

        # Right Left Case
        if balance < -1 and new_node.value < current_node.get_right().value:
            current_node.add_right(self._right_rotate(current_node.get_right()))
            return self._left_rotate(current_node)

        return current_node

    def _left_rotate(self, z):
        y = z.get_right()
        T2 = y.get_left()

        # Perform rotation
        y.add_left(z)
        z.add_right(T2)

        # Update heights
        z.height = 1 + max(self._get_height(z.get_left()), self._get_height(z.get_right()))
        y.height = 1 + max(self._get_height(y.get_left()), self._get_height(y.get_right()))

        # Return the new root
        return y

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        if node is None:
            return node

        # Paso 1: Eliminar el nodo
        if value < node.value:
            node.add_left(self._delete_recursively(node.get_left(), value))
        elif value > node.value:
            node.add_right(self._delete_recursively(node.get_right(), value))
        else:
            # Nodo con un hijo o sin hijos
            if node.get_left() is None:
                return node.get_right()
            elif node.get_right() is None:
                return node.get_left()
            # Nodo con dos hijos: obtener el sucesor
            temp = self._get_min_value_node(node.get_right())
            node.value = temp.value
            node.add_right(self._delete_recursively(node.get_right(), temp.value))

        # Paso 2: Actualizar altura
        node.height = 1 + max(self._get_height(node.get_left()), self._get_height(node.get_right()))

        # Paso 3: Balancear el nodo
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and self._get_balance(node.get_left()) >= 0:
            return self._right_rotate(node)
        # Left Right
        if balance > 1 and self._get_balance(node.get_left()) < 0:
            node.add_left(self._left_rotate(node.get_left()))
            return self._right_rotate(node)
        # Right Right
        if balance < -1 and self._get_balance(node.get_right()) <= 0:
            return self._left_rotate(node)
        # Right Left
        if balance < -1 and self._get_balance(node.get_right()) > 0:
            node.add_right(self._right_rotate(node.get_right()))
            return self._left_rotate(node)

        return node

    def _get_min_value_node(self, node):
        current = node
        while current.get_left() is not None:
            current = current.get_left()
        return current