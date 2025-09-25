def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

array1 = [5,4,3,2,1]
array2 = [-5,2,4,-12,0,4,7]
selection_sort(array1)
selection_sort(array2)

print(array1)
print(array2)

# Time complexity O(n^2) - Not the best in sorting algorithms
# Space complexity O(1) - Really useful in low memory scenarios
