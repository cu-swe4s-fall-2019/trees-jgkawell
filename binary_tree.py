class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, key, value=None):
        self.root = None
        self.root = self.insert(key, value)

    def insert(self, key, value=None):
        # Simple insert call for users
        if isinstance(key, int):
            return self.insert_by_value(self.root, key, value)
        else:
            raise TypeError("Keys must be integers")

    def insert_by_value(self, node, key, value=None):
        if node is None:
            # Create the a new node
            node = Node(key, value=value)
        elif node.key == key:
            # Ignore duplicate keys
            return node
        else:
            if key < node.key:
                # Insert recursively on left branch
                node.left = self.insert_by_value(node.left, key, value=value)
            else:
                # Insert recursively on right branch
                node.right = self.insert_by_value(node.right, key, value=value)

        # Return the updated node
        return node


def insert(root, key, value=None):
    return root


def search(root, key):
    return None
