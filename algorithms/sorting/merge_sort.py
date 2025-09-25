def merge_sorted_arrays(left_array, right_array):
    l = 0
    r = 0

    final_array = [0] * (len(left_array) + len(right_array))
    i = 0
    while l < len(left_array) and r < len(right_array):
        if left_array[l] < right_array[r]:
            final_array[i] = left_array[l]
            l += 1
        else:
            final_array[i] = right_array[r]
            r += 1
        i += 1

    
    while l >= len(left_array) and r < len(right_array):
        final_array[i] = right_array[r]
        r +=1
        i += 1

    while r >= len(right_array) and l < len(left_array):
        final_array[i] = left_array[l]
        l +=1
        i += 1
    
    return final_array


def merge_sort(nums):
    l = 0
    r = len(nums)
    if len(nums) == 1:
        return nums
    
    mid = (l + r) // 2

    left_side = nums[:mid]
    right_side = nums[mid:]

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    
    return merge_sorted_arrays(left_side, right_side)




array = [-5,2,4,-12,0,4,7]
array2 = [5,2,3,1]
array3 = [5,1,1,2,0,0]

merged = merge_sort(array)
merged2 = merge_sort(array2)
merged3 = merge_sort(array3)

print(merged)
print(merged2)
print(merged3)

# Time complexity O(n*logn) - One of the best sorting algorithms in terms of time complexity
# Space complexity O(n) - Could be O(logn), but its harder to implement 