class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        # Simple insert call for users
        if isinstance(key, int):
            self.root = self.insert_by_value(self.root, key, value)
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

    def search(self, key):
        # Simple search call for users
        if isinstance(key, int):
            return self.search_by_value(self.root, key)
        else:
            raise TypeError("Keys must be integers")

    def search_by_value(self, node, key):
        if node is None:
            # Couldn't find key, return None
            value = None
        elif node.key == key:
            # Found key, return value
            value = node.value
        else:
            if key < node.key:
                # Recursively search left
                value = self.search_by_value(node.left, key)
            else:
                # Recursively search right
                value = self.search_by_value(node.right, key)

        # Return value to user
        return value


if __name__ == '__main__':

    tree = BinaryTree(10, '-')
    tree.insert(9, 'a')
    tree.insert(15, 'b')
    tree.insert(11, 'c')

    print(tree.root.key, tree.root.value)
    print(tree.root.left.key, tree.root.left.value)
    print(tree.root.right.left.key, tree.root.right.left.value)

    print(tree.search(10))
    print(tree.search(9))
    print(tree.search(15))
    print(tree.search(11))
    print(tree.search(1))
