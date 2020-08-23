List = [2, 1, 10, 7, 9, 8, 5, 4, 6, 3]


def linearSearch(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None


print(linearSearch(List, 7))
