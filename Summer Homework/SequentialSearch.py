List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def sequentialSearch(list, item):
    for i in range(len(list)):
        if list[i] > item:
            return None
        elif list[i] == item:
            return i


print(sequentialSearch(List, 7))
