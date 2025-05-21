def find_biggest(int_list: list) -> int | None:
    if len(int_list) == 0:
        return None
    if len(int_list) == 2:
        return int_list[0] if int_list[0] > int_list[1] else int_list[1]
    sub_max = find_biggest(int_list[1:])
    return int_list[0] if int_list[0] > sub_max else sub_max

print(find_biggest([5,2,1,4,3]))
