import argparse
import sys
import csv
import time
from binary_tree import *
sys.path.insert(1, "./hash-tables-jgkawell/")
sys.path.insert(1, "./avl_tree/")
from hash_tables import *  # noqa: E402
from hash_functions import *  # noqa: E402
from avl import *  # noqa: E402


parser = argparse.ArgumentParser(
    description='Test performance of different key/value data structures.')
parser.add_argument(
    '--data_structure',
    type=str,
    help='The data structure to use (hash, avl, or tree)')
parser.add_argument(
    '--dataset',
    type=str,
    help='The the data set to use (rand.txt or sorted.txt)')
parser.add_argument(
    '--num_data',
    type=int,
    help='The amount of data to use')


def insert_items_hash(data, num_data):
    table = LinearProbe(100, h_ascii)
    count = 0
    for pair in data:
        table.add(str(pair[0]), pair[1])
        count += 1
        if count == num_data:
            break
    return table


def search_items_hash(table, data, num_data):
    count = 0
    for pair in data:
        table.search(str(pair[0]))
        count += 1
        if count == num_data:
            break


def insert_items_avl(data, num_data):
    avl = AVL()
    count = 0
    for pair in data:
        avl.insert(pair[0])
        count += 1
        if count == num_data:
            break
    return avl


def search_items_avl(avl, data, num_data):
    count = 0
    for pair in data:
        avl.find(pair[0])
        count += 1
        if count == num_data:
            break


def insert_items_tree(data, num_data):
    tree = BinaryTree()
    count = 0
    for pair in data:
        tree.insert(pair[0], pair[1])
        count += 1
        if count == num_data:
            break
    return tree


def search_items_tree(tree, data, num_data):
    count = 0
    for pair in data:
        tree.search(pair[0])
        count += 1
        if count == num_data:
            break


def get_data(file_name):
    pairs_list = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            pairs_list.append((int(row[0]), int(row[1])))
    return pairs_list


def main():
    """
    Runs all the needed functions.
    """

    # Parse args and read in data from the files
    args = parser.parse_args()

    # Read data from data file
    data = get_data(args.dataset)

    # Run tests based on data structure
    if args.data_structure == "hash":
        # Use hash table
        start = time.time()
        table = insert_items_hash(data, args.num_data)
        end = time.time()
        print("Insert time elapsed: ", (end - start))

        start = time.time()
        search_items_hash(table, data, args.num_data)
        end = time.time()
        print("Search time elapsed: ", (end - start))
    elif args.data_structure == "avl":
        # Use AVL tree
        start = time.time()
        avl = insert_items_avl(data, args.num_data)
        end = time.time()
        print("Insert time elapsed: ", (end - start))

        start = time.time()
        search_items_avl(avl, data, args.num_data)
        end = time.time()
        print("Search time elapsed: ", (end - start))
    elif args.data_structure == "tree":
        # Use binary search tree
        start = time.time()
        tree = insert_items_tree(data, args.num_data)
        end = time.time()
        print("Insert time elapsed: ", (end - start))

        start = time.time()
        search_items_tree(tree, data, args.num_data)
        end = time.time()
        print("Search time elapsed: ", (end - start))
    else:
        print("ERROR: data structure must be hash, avl or tree.")
        sys.exit(1)


if __name__ == '__main__':
    main()
