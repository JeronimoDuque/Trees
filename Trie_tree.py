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
        current_node.is_end = True
    

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                # Fin de la palabra
                if not node.is_end:
                    return False  # La palabra no existe
                node.is_end = False
                return len(node.children) == 0  # Si no tiene hijos, se puede borrar
            char = word[depth]
            child = node.children.get(char)
            if child is None:
                return False  # La palabra no existe
            should_delete_child = _delete(child, word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not getattr(node, 'is_end', False)
            return False

        # Marca el final de palabra en Node si no existe
        if not hasattr(self.root, 'is_end'):
            def mark_end(node):
                node.is_end = False
                for child in node.children.values():
                    mark_end(child)
            mark_end(self.root)

        _delete(self.root, word, 0)

    def search(self, word):
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end


    def visualize(self):
        if self.root is None:
            print("El árbol está vacío.")
            return

        G = nx.DiGraph()
        labels = {}

        def add_edges(node, parent_label=None):
            node_label = f"{node.char}\n({'End' if node.is_end else 'Not End'})"
            labels[node_label] = node.char
            if parent_label:
                G.add_edge(parent_label, node_label)
            for child in node.children.values():
                add_edges(child, node_label)

        add_edges(self.root)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, labels=labels, arrows=True, node_size=2000, node_color='lightblue', font_size=10)
        plt.title("Visualización del Trie")
        plt.show()
