# Maximum Subarray Sum (Kadane’s Algorithm)

## Problem

Given an array of integers (positive, negative, or zero), find the contiguous subarray that has the largest sum.  
If all sums are negative, return `0`.

---

## Key Idea

Instead of checking all possible subarrays (**O(n²)**), track the best subarray **ending at each position** in a single pass (**O(n)**).  
Maintain:

- `current_sum` → maximum sum ending at the current element
- `max_sum` → maximum sum found so far

---

## Algorithm

1. Initialize:

   ```python
   current_sum = 0
   max_sum = 0

   ```

2. For each element **num** in the array
   - Update:
   ```python
   current_sum = max(num, current_sum + num)
   ```
   - Decide whether to start fresh at **num** or extedend the previous sum
   - If **current_sum < 0**, reset it to **0** (negatives reduce future sums)
   - Update:
   ```python
   max_sum = max(max_sum, current_sum)
   ```
   - return **max_sum**

## Complexity

- **Time: O(n)** — single loop over the array
- **Space: O(1)** — only a few variables stored
