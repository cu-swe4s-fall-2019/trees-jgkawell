import unittest
import binary_tree
import random


class TestBinaryTree(unittest.TestCase):
    def test_basic_add(self):
        tree = binary_tree.BinaryTree(10, 'a')
        tree.insert(15, 'b')
        tree.insert(-5, 'c')
        tree.insert(12, 'd')

        self.assertEqual(tree.root.key, 10)
        self.assertEqual(tree.root.left.key, -5)
        self.assertEqual(tree.root.right.left.key, 12)

    def test_duplicate_insert(self):
        tree = binary_tree.BinaryTree(10, 'a')
        tree.insert(15, 'b')
        tree.insert(5, 'c')
        tree.insert(12, 'd')
        tree.insert(12, 'e')

        self.assertEqual(tree.root.right.left.value, 'd')

    def test_non_num_key_on_insert(self):
        tree = binary_tree.BinaryTree(10, 'a')
        tree.insert(15, 'b')
        tree.insert(5, 'c')
        tree.insert(12, 'd')

        with self.assertRaises(TypeError) as ex:
            tree.insert("not int", 'e')

        self.assertEqual(
            str(ex.exception), "Keys must be integers")

    def test_random_insert_and_search(self):
        tree = binary_tree.BinaryTree(1, 'a')

        entries = {}
        for i in range(0, 100):
            key = random.randint(-1000, 1000)
            value = random.randint(-1000, 1000)
            tree.insert(key, value)

        for key, value in entries.items():
            self.assertEqual(tree.search(key), value)

    def test_non_num_key_on_search(self):
        tree = binary_tree.BinaryTree(10, 'a')
        tree.insert(15, 'b')
        tree.insert(5, 'c')
        tree.insert(12, 'd')

        with self.assertRaises(TypeError) as ex:
            tree.search("not int")

        self.assertEqual(
            str(ex.exception), "Keys must be integers")


if __name__ == '__main__':
    unittest.main()
