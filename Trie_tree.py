from Node import Node

import networkx as nx
import matplotlib.pyplot as plt

class Trie_tree:
    def __init__(self):
        self.root = Node("")  # Root node doesn't hold any character

    def insert(self, word):
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                new_node = Node(char)
                current_node.children[char] = new_node
            current_node = current_node.children[char]
    
    def __str__(self):
        def traverse(node, prefix, depth):
            result = "  " * depth + repr(node.data) + "\n"
            for child in node.children.values():
                result += traverse(child, prefix + child.data, depth + 1)
            return result
        return traverse(self.root, "", 0)


    def visualize(self):
        G = nx.DiGraph()
        levels = {}

        def add_edges(node, parent_id, level, x_pos):
            node_id = id(node)
            G.add_node(node_id, label=node.data)
            levels.setdefault(level, []).append(node_id)
            if parent_id is not None:
                G.add_edge(parent_id, node_id)
            for i, child in enumerate(node.children.values()):
                add_edges(child, node_id, level + 1, i)

        add_edges(self.root, None, 0, 0)

        # Calcular posiciones por nivel
        pos = {}
        for level, nodes in levels.items():
            n = len(nodes)
            for i, node_id in enumerate(nodes):
                pos[node_id] = (i - n / 2, -level)  # x: horizontal, y: nivel negativo

        labels = nx.get_node_attributes(G, 'label')
        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, labels=labels, node_color='lightblue', arrows=True, with_labels=True)
        plt.title("Trie Visualization por niveles")
        plt.show()


tree = Trie_tree()
tree.insert("hello")
tree.insert("hi")
tree.insert("hey")

print(tree)
tree.visualize()

