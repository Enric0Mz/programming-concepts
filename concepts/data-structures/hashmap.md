# Overview

Hashmaps are commonly featured in many programming languages. In Python, they are implemented as dictionaries, a data structure that stores key-value pairs.

## Talking about basic operations complexity

- Inserting, Deleting, and Reading: These operations typically have a time complexity of O(1) because you can directly access the correct compartment using the key. In the worst-case scenario, the complexity becomes O(n) due to collisions, which occur when multiple items are assigned to the same compartment, requiring additional storage or resolution.

## Example

student_grades = {
"Alice": 85,
"Bob": 92,
"Charlie": 78
}
