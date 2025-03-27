def binary_search(nums_list: list[int], num: int): # Temporal O(logN) Spacial O(1)
    left = 0
    right = len(nums_list)
    steps = 0 # To check temporal complexity

    while left < right:
        steps += 1
        mid = int((left+right) / 2)

        if nums_list[mid] == num:
            print(f"{num} founded in step {steps}")
            return nums_list[mid]
        elif nums_list[mid] < num:
            left = mid + 1
        else:
            right = mid
    return -1


lista1 = [1, 2, 3, 4, 5]

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

binary_search(lista1, 3)
print("...")
binary_search(lista2, 3)
print("...")
binary_search(lista3, 3)
print("...")
binary_search(lista4, 3)
