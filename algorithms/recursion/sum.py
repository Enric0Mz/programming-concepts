def sum_recursive(int_list: int) -> int:
    if int_list == []:
        return 0
    return int_list[0] + sum_recursive(int_list[1:])


print(sum_recursive([1,2,3,4,5]))