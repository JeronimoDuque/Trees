import networkx as nx
import matplotlib.pyplot as plt

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grado mínimo
        self.leaf = leaf
        self.keys = []
        self.children = []

    def split_child(self, i, y):
        t = self.t
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]  # Copia las claves mayores al nuevo nodo
        mid_key = y.keys[t-1]  # Guarda la clave del medio
        y.keys = y.keys[:t-1]  # El hijo original se queda con las claves menores
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, mid_key)  # Inserta la clave del medio en el padre

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i, self.children[i])
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def find_key(self, key):
        for i, k in enumerate(self.keys):
            if k >= key:
                return i
        return len(self.keys)

    def remove(self, key):
        idx = self.find_key(key)
        if idx < len(self.keys) and self.keys[idx] == key:
            if self.leaf:
                self.keys.pop(idx)
            else:
                self.remove_from_internal_node(idx)
        else:
            if self.leaf:
                return  # El key no está en el árbol
            flag = idx == len(self.keys)
            if len(self.children[idx].keys) < self.t:
                self.fill(idx)
            if flag and idx > len(self.keys):
                self.children[idx - 1].remove(key)
            else:
                self.children[idx].remove(key)

    def remove_from_internal_node(self, idx):
        key = self.keys[idx]
        if len(self.children[idx].keys) >= self.t:
            pred = self.get_predecessor(idx)
            self.keys[idx] = pred
            self.children[idx].remove(pred)
        elif len(self.children[idx + 1].keys) >= self.t:
            succ = self.get_successor(idx)
            self.keys[idx] = succ
            self.children[idx + 1].remove(succ)
        else:
            self.merge(idx)
            self.children[idx].remove(key)

    def get_predecessor(self, idx):
        current = self.children[idx]
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]

    def get_successor(self, idx):
        current = self.children[idx + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]

    def fill(self, idx):
        if idx != 0 and len(self.children[idx - 1].keys) >= self.t:
            self.borrow_from_prev(idx)
        elif idx != len(self.keys) and len(self.children[idx + 1].keys) >= self.t:
            self.borrow_from_next(idx)
        else:
            if idx != len(self.keys):
                self.merge(idx)
            else:
                self.merge(idx - 1)

    def borrow_from_prev(self, idx):
        child = self.children[idx]
        sibling = self.children[idx - 1]
        child.keys.insert(0, self.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        self.keys[idx - 1] = sibling.keys.pop()

    def borrow_from_next(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]
        child.keys.append(self.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        self.keys[idx] = sibling.keys.pop(0)

    def merge(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]
        child.keys.append(self.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        self.children.pop(idx + 1)

class B_tree:
    def __init__(self, t):
        self.root = None
        self.t = t  # Grado mínimo

    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.split_child(0, self.root)
                idx = 0
                if s.keys[0] < key:
                    idx += 1
                s.children[idx].insert_non_full(key)
                self.root = s
            else:
                self.root.insert_non_full(key)

    def delete(self, key):
        if not self.root:
            return
        self.root.remove(key)
        if len(self.root.keys) == 0:
            if self.root.leaf:
                self.root = None
            else:
                self.root = self.root.children[0]

    def visualize(self):
        def add_nodes_edges(node, G, parent_id=None):
            node_id = str(id(node))
            label = "|".join(str(k) for k in node.keys)
            G.add_node(node_id, label=label)
            if parent_id:
                G.add_edge(parent_id, node_id)
            for child in node.children:
                add_nodes_edges(child, G, node_id)

        G = nx.DiGraph()
        if self.root:
            add_nodes_edges(self.root, G)

        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')
        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color='lightblue', font_size=10)
        plt.title("Visualización del B-tree con NetworkX")
        plt.show()
