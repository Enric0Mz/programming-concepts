def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j-1] = nums[j - 1], nums[j]
            else:
                break

array1 = [1,3,2,6,5,3]
array2 = [-5,2,4,-12,0,4,7]
insertion_sort(array1)
insertion_sort(array2)
print(array1)
print(array2)

# Time complexity O(n^2) - Not the best in sorting algorithms
# Space complexity O(1) - Really useful in low memory scenarios