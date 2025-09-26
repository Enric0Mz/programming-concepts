def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[-1]
    
    left = [x for x in nums[:-1] if x < pivot]
    right = [x for x in nums[:-1] if x >= pivot]

    print("LEFT", left, "PIVOT", [pivot], "RIGHT", right)


    l = quick_sort(left)
    r = quick_sort(right)

    return l + [pivot] + r 


array1 = [5,4,2,6,3,9,1]
quick = quick_sort(array1)

print(quick)

# Time complexity O(n*logn) - In the worst cases, can become O(n^2)
# Space complexity O(n) - Could be O(logn), but its harder to implement