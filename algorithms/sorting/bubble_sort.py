def bubble_sort(nums_list: list):
    counter = 1
    for _ in nums_list:
        is_sorted = True
        print(f"Lista no passo {counter}: {nums_list}")
        counter += 1
        for j in range(len(nums_list) - 1):
            if nums_list[j] > nums_list[j+1]:
                is_sorted = False
                nums_list[j], nums_list[j+1] = nums_list[j+1], nums_list[j]
        
        if is_sorted:
            return

bubble_sort([5,4,3,2,1])
print("...")
bubble_sort([1,2,3,5,4])
print("...")
bubble_sort([1,2,3,4,5])