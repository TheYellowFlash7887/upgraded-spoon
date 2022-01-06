import typing


def mergesort(input_list: list) -> list:
    midpoint = len(input_list) // 2
    left_list = input_list[:midpoint]
    right_list = input_list[midpoint:]
    if len(left_list) >= 2:
        # left list is now sorted
        left_list = mergesort(left_list)
    if len(right_list) > 2:
        # right list is now sorted
        right_list = mergesort(right_list)
    return merged(left_list, right_list)


def merged(left: list, right: list) -> list:
    merged_lists: list = left + right
    return sorted(merged_lists)


if __name__ == '__main__':
    input1 = [10, 2, 5, 6, 15, 17, 99, 107, 8]
    print(mergesort(input1))
