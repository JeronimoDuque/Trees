from Node_binary import Node_binary

class Binary_tree:
    def __init__(self):
        self.root = None

    def preorder_with_position(self, value, node=None, pos=None, result=None):
        if pos is None:
            pos = [0]
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node:
            pos[0] += 1
            if node.data == value:
                result.append((node.data, pos[0]))
            self.preorder_with_position(value, node.left, pos, result)
            self.preorder_with_position(value, node.right, pos, result)
        return result

    def inorder_with_position(self, value, node=None, pos=None, result=None):
        if pos is None:
            pos = [0]
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node:
            self.inorder_with_position(value, node.left, pos, result)
            pos[0] += 1
            if node.data == value:
                result.append((node.data, pos[0]))
            self.inorder_with_position(value, node.right, pos, result)
        return result

    def postorder_with_position(self, value, node=None, pos=None, result=None):
        if pos is None:
            pos = [0]
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node:
            self.postorder_with_position(value, node.left, pos, result)
            self.postorder_with_position(value, node.right, pos, result)
            pos[0] += 1
            if node.data == value:
                result.append((node.data, pos[0]))
        return result