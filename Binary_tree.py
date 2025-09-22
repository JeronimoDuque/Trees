from Node_binary import Node_binary

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