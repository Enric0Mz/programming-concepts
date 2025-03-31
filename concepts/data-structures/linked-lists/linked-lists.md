## Overview

In a linked list, each item can be stored at a different location in memory, but every item knows the location of the next one through pointers. To traverse the entire list, you must start at the head and visit each item sequentially.

## Talking about basic operations complexity

- Insert or Remove at the Head: Adding or removing an item at the head only requires updating the head pointer and, if necessary, the next pointer of the new head. This is an O(1) operation.
- Access a Specific Resource: To access a specific item, you must traverse the list from the head, visiting each item until you reach the desired one, making this an O(n) operation.
- Insert or Remove at the Middle or Tail: Inserting or removing an item in the middle or at the tail requires traversing the list to find the correct position and then updating the pointers, resulting in an O(n) operation.
