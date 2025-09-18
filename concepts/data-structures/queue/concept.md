# Overview

A Queue is a linear data structure that follows the FIFO (First-In, First-Out) principle, much like a real-life supermarket line, for example. In this structure, the first item added is always the first item to be removed.

## Operations

- Enqueue - Adds an item to the end of the queue. If the queue is full, a "Queue Overflow" error occurs. Time complexity: O(1).

- Dequeue - Removes the first item from the queue, which was consequently the first one to be added. If the queue is empty, a "Queue Underflow" error occurs. Time complexity: O(1).

- Peek - Returns the first item from the queue without removing it. Time complexity: O(1).

- isEmpty - Returns true or false to check if the queue is empty. Time complexity: O(1).

## Examples

Queues are very useful in algorithms like Breadth-First Search (BFS) and Level Order Traversal. Additionally, they contribute to applications such as packet buffering and load balancing.
