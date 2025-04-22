# Binary Trees

## Overview

A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the _left child_ and _right child_. Binary trees are commonly used for hierarchical data storage, efficient searching, and expression parsing. Unlike linked lists, binary trees allow for more structured and efficient searching and insertion when balanced properly.

Each node in the tree contains:

- A value.
- A pointer to the left child.
- A pointer to the right child.

Traversal can be performed in multiple ways:

- **In-Order (Left, Root, Right)** – typically used for binary search trees (BST) to retrieve data in sorted order.
- **Pre-Order (Root, Left, Right)** – used to create a copy of the tree.
- **Post-Order (Left, Right, Root)** – used to delete the tree.
- **Level-Order (Breadth-First)** – visits nodes level by level.

## Talking about basic operations complexity

- **Insertion**:  
  In a binary search tree (BST), insertion requires finding the appropriate leaf position based on value comparison, which takes O(log n) time in a balanced tree. In the worst case (completely unbalanced), it degrades to O(n).

- **Deletion**:  
  Deleting a node involves three main cases:

  1. Node is a leaf – simply remove it.
  2. Node has one child – replace it with its child.
  3. Node has two children – find the in-order successor or predecessor, replace the node's value, and remove the successor/predecessor node.
     The complexity is O(log n) in a balanced tree, and O(n) in the worst case.

- **Search**:  
  Similar to insertion, searching in a binary search tree is O(log n) in a balanced case, and O(n) in the worst-case (unbalanced).

- **Traversal**:  
  Traversing the entire tree (regardless of order) is O(n), since each node must be visited once.
