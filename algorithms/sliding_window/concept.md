## Sliding Window

Sliding window is an algorithmic technique, typically implemented on Arrays or Strings, which uses a "window" of items to perform a certain action. It is very common in problems that need to find a substring or subarray based on a specific condition, avoiding recalculation (usually associated with brute-force approaches) to solve the problem.

The two main patterns in which the sliding window is used:

- **Variable Size**
  In variable-sized window problems, the task is usually to find the longest or shortest subarray that satisfies a certain condition, such as the "longest substring without repeating characters" or the "longest subarray where the sum of elements is less than 10."

- **Fixed Size**
  In fixed-sized window problems, the task usually asks to find something related to a subarray of a specific size `k`. For example, returning the subarray of size `k` that has the largest sum in the entire array.

## Complexity

The sliding window algorithm typically has a time complexity of $O(n)$. This is because even while expanding and shrinking the window, both pointers (or the window bounds) only move in one direction (usually to the right).

As for its space complexity, it can vary significantly between $O(n)$ and $O(1)$, depending on the specific requirements of the problem (e.g., storing characters in a hash map).
