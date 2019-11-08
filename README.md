# trees
Basic Tree Data Structure Demo

## Description
This repository demonstrates the usage of a binary search tree for storing key/value pairs of data. The basic implementation accepts integer key values and stores them in a binary tree along with their corresponding (optional) values. This repo also contains a script that allows the benchmarking of different data structures including hash tables, AVL trees, and basic binary search trees.

## How to use
You can use this as a standard python library by importing the binary tree script and using the provided tree class:

```
from binary_tree import *

tree = BinaryTree()
tree.insert(10, 'abc')
tree.search(10)
>>> abc
```

You can also benchmark the different data structures using the provided script. It has the below options as flags:

```
Test performance of different key/value data structures.

optional arguments:
  -h, --help            show this help message and exit
  --data_structure DATA_STRUCTURE
                        The data structure to use (hash, avl, or tree)
  --dataset DATASET     The the data set to use (rand.txt or sorted.txt)
  --num_data NUM_DATA   The amount of data to use
```

## Benchmarking
The above mentioned script was used to benchmark the different data structures using both randomized and sorted data. The results are below:

```
-- Randomized --
hash
('Insert time elapsed: ', 0.07384300231933594)
('Search time elapsed: ', 0.05452895164489746)
avl
('Insert time elapsed: ', 0.009997129440307617)
('Search time elapsed: ', 0.0012969970703125)
tree
('Insert time elapsed: ', 0.002218008041381836)
('Search time elapsed: ', 0.0016028881072998047)

-- Sorted --
hash
('Insert time elapsed: ', 0.08244800567626953)
('Search time elapsed: ', 0.06673502922058105)
avl
('Insert time elapsed: ', 0.01057887077331543)
('Search time elapsed: ', 0.0009658336639404297)
tree
('Insert time elapsed: ', 0.014908075332641602)
('Search time elapsed: ', 0.012033939361572266)
```

The most interesting thing to note here is that while the binary search tree was the fastest all around in the randomized case, the AVL tree boasted a much faster search time in the sorted case due to the fact that it balances it's data as it inserts.

## Installation
The installation is simple. Clone the repository and then initialize the submodules to enable the usage of the hash tables and AVL trees.

```
git submodule update --init
```
