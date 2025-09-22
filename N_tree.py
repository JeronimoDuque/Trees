from Node import Node

class N_tree:
    def __init__(self):
        self.root = None

    def insert(self, parent_value, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == parent_value:
                node.children.append(new_node)
                return True
            queue.extend(node.children)
        return False  # parent_value no encontrado

    def delete(self, value):
        if self.root is None:
            return False
        if self.root.value == value:
            self.root = None
            return True
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            for child in node.children:
                if child.value == value:
                    node.children.remove(child)
                    return True
            queue.extend(node.children)
        return False  # valor no encontrado

    def search_level_order(self, value):
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return True
            queue.extend(node.children)
        return False

    def get_level_order_list(self):
        result = []
        if self.root is None:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            queue.extend(node.children)
        return result