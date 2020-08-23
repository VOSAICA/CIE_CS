List = [2, 1, 10, 7, 9, 8, 5, 4, 6, 3]


def bubbleSort(list):
    stop = len(list) - 1
    for j in range(stop):
        noMore = True
        for i in range(stop):
            if list[i] > list[i + 1]:
                list[i + 1], list[i] = list[i], list[i + 1]
                noMore = False
        if noMore:
            break
        stop -= 1
    return list


print(bubbleSort(List))
