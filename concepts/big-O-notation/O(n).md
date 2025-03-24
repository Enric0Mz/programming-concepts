# Overview

## Time Complexity (Temporal)

O(N) is one of the simplest complexities to understand because it means that the algorithm's execution time grows proportionally to the size of the input. If the size of an array increases, the time required to process it also increases at the same rate.

## Memory Complexity (Spatial)

The same concept applies to memory complexity. If an algorithm requires storing additional variables based on the size of an array, the memory usage will grow proportionally to the array's size.

# Examples

## Time Complexity (Temporal)

An easy-to-understand example is an algorithm that doubles the value of every number in an array.

- If the array has 10 elements, the operation is performed 10 times → O(10).

- If the array has 100 elements, the operation is performed 100 times → O(100).

In general, for an array of size N, the algorithm runs N operations, making its time complexity O(N).

## Memory Complexity (Spatial)

The same logic applies to memory complexity. If you need to store the calculated values in a new array, the memory required grows proportionally to the size of the input array.

- If the original array has 10 elements, the new array will also have 10 elements → O(10).

- If the original array has 100 elements, the new array will have 100 elements → O(100).

Thus, the memory complexity is O(N) because storage requirements increase linearly with input size.
