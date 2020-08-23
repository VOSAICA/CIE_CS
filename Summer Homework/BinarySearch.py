List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def binarySearch(list, item):
    lower = 0
    higher = len(list) - 1
    while lower <= higher:
        middle = int((lower + higher) / 2)
        if list[middle] == item:
            return middle
        elif list[middle] < item:
            lower = middle + 1
        else:
            higher = middle - 1
    return None


print(binarySearch(List, 0))
