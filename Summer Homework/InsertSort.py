List = [2, 1, 10, 7, 9, 8, 5, 4, 6, 3]


def insertSort(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            temp = list[i]
            for j in range(i - 1, -1, -1):
                if list[j] > temp:
                    list[j + 1], list[j] = list[j], list[j + 1]
                else:
                    break
    return list


print(insertSort(List))
