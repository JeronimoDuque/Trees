from Node import Node
import networkx as nx
import matplotlib.pyplot as plt

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
    
    def visualize(self):
        def add_nodes_edges(node, G, parent_id=None):
            if node is None:
                return
            node_id = str(id(node))
            label = str(node.value)
            G.add_node(node_id, label=label)
            if parent_id:
                G.add_edge(parent_id, node_id)
            for child in node.children:
                add_nodes_edges(child, G, node_id)

        G = nx.DiGraph()
        if self.root:
            add_nodes_edges(self.root, G)

        pos = nx.spring_layout(G)  # Layout automático
        labels = nx.get_node_attributes(G, 'label')

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, labels=labels,
                node_size=2000, node_color='lightgreen', font_size=10)
        plt.title("Visualización del Árbol N-ario")
        plt.show()