MyLists = [2, 1, 4, 6, 5, 8, 10, 7, 9, 3]
Stop = len(MyLists) - 1
NoMore = True
for j in range(Stop):
    NoMore = True
    for i in range(Stop):
        if MyLists[i] > MyLists[i + 1]:
            MyLists[i + 1], MyLists[i] = MyLists[i], MyLists[i + 1]
            NoMore = False
    if NoMore is True:
        break
    Stop -= 1
print(MyLists)
