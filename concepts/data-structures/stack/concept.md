# Overview

A stack is a linear data structure that stores items following the LIFO (Last-In-First-Out) principle. It works like a real-world stack of plates, where the last items added are the first to be removed.

## Operations

Push: In this operation, items are added to the top of the stack. It has a time complexity of O(1) because we always keep track of the stack's size or, depending on the implementation, the top element.

Pop: This operation removes the last item added to the stack, following the LIFO principle. It also has a time complexity of O(1).

Peek: An operation that only returns the top item of the stack without removing it. Its time complexity is also O(1).

Is Empty: As the name suggests, this operation returns True if there are no items on the stack, and False otherwise. It is very useful to assist in the implementation of pop and peek operations. The time complexity is O(1).

## Examples

Stacks are very powerful in solving algorithms, such as those using monotonic stacks, to store values and perform operations with them. They are widely used in everyday applications like code linters, programming language call stacks, and browser history.
