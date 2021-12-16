import typing


def mergesort(inputlist: list) -> list:
    print(inputlist)
    middle: int = len(inputlist)//2
    left_list: list = inputlist[:middle]
    right_list: list = inputlist[middle:]
    print(left_list, right_list)


def merge(left: list, right: list) -> list:
    pass


if __name__ == '__main__':
    input1 = ['10', '2', '5', '6', '15', '17', '99', '107', ' 8']
    print(mergesort(input1))
