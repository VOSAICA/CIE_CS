NumberOfRows = int(input("input the row of the grid: "))
NumberOfColumns = int(input("input the Column of the grid: "))
symbol = input("input the symbol: ")
for i in range(NumberOfRows):
    print(symbol * NumberOfColumns)
