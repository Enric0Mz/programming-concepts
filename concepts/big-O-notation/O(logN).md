# Overview

## Time Complexity (Temporal)

When we talk about O(log N), it is important to understand the mathematical logic behind logarithms. For example, log2(10) = 3.32, log2(20) = 4.32, and log2(40) = 5.32. Notice that when the input value doubles, the logarithmic result increases only slightly. The same concept applies to Big-O notation: if the size of a given array doubles, and the algorithm has O(log N) complexity, the time required to complete the operation increases only by a small amount, rather than doubling.

# Examples

## Time Complexity (Temporal)

The most common example is the binary search, where, given an ordenated array, you need to find some element. You always need to point the middle of the array, and if the value you aiming is bigger than the value in middle, you go to the middle of the bigger portion, and repeat that till you find the desirable value. If the size of the array doubles, for example, the number of steps you will need to perform to find the value increases by a tiny, not doubles.
