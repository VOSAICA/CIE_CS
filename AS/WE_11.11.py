MyLists = [0, 1, 2, 3, 4, 5, 6]
SearchValue = int(input("input the number you would like to find:"))
for i in range(len(MyLists)):
    if SearchValue == MyLists[i]:
        print("Value had been found, it is the number ", i+1, "th")
        exit()
print("Value not found")
