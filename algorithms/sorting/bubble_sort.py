def bubble_sort(nums):
    size = len(nums)
    is_sorted = True

    for _ in nums:
        for j in range(size - 1):
            if nums[j] > nums[j + 1]:
                is_sorted = False
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if is_sorted:
            return
    
array1 = [5,4,3,2,1]
array2 = [5,4,3,2,1]
array3 = [5,4,3,2,1]
bubble_sort(array1)
bubble_sort(array2)
bubble_sort(array3)
print(array1)
print(array2)
print(array3)


# Time complexity O(n^2) - Not the best in sorting algorithms
# Space complexity O(1) - Really useful in low memory scenarios