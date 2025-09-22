from Node_binary import Node_binary
import networkx as nx
import matplotlib.pyplot as plt

class Binary_tree:
    def __init__(self):
        self.root = None

    def preorder_with_position(self, value, node=None, pos=None, result=None, found=None):
        if pos is None:
            pos = [0]
        if result is None:
            result = []
        if found is None:
            found = []
        if node is None:
            node = self.root
        if node:
            pos[0] += 1
            result.append(node.data)
            if node.data == value:
                found.append(pos[0])
            self.preorder_with_position(value, node.left, pos, result, found)
            self.preorder_with_position(value, node.right, pos, result, found)
        return result, found

    def inorder_with_position(self, value, node=None, pos=None, result=None, found=None):
        if pos is None:
            pos = [0]
        if result is None:
            result = []
        if found is None:
            found = []
        if node is None:
            node = self.root
        if node:
            self.inorder_with_position(value, node.left, pos, result, found)
            pos[0] += 1
            result.append(node.data)
            if node.data == value:
                found.append(pos[0])
            self.inorder_with_position(value, node.right, pos, result, found)
        return result, found

    def postorder_with_position(self, value, node=None, pos=None, result=None, found=None):
        if pos is None:
            pos = [0]
        if result is None:
            result = []
        if found is None:
            found = []
        if node is None:
            node = self.root
        if node:
            self.postorder_with_position(value, node.left, pos, result, found)
            self.postorder_with_position(value, node.right, pos, result, found)
            pos[0] += 1
            result.append(node.data)
            if node.data == value:
                found.append(pos[0])
        return result, found


    def visualize(self):
        def add_nodes_edges(node, G, parent_id=None):
            if node is None:
                return
            node_id = str(id(node))  # ID único para cada nodo
            label = str(node.value)  # Valor del nodo
            G.add_node(node_id, label=label)

            if parent_id:
                G.add_edge(parent_id, node_id)

            # hijos izquierdo y derecho
            add_nodes_edges(node.left, G, node_id)
            add_nodes_edges(node.right, G, node_id)

        G = nx.DiGraph()
        if self.root:
            add_nodes_edges(self.root, G)

        pos = nx.spring_layout(G)  # Layout automático
        labels = nx.get_node_attributes(G, 'label')

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, labels=labels,
                node_size=2000, node_color='lightblue', font_size=10)
        plt.title("Visualización del Árbol Binario")
        plt.show()
