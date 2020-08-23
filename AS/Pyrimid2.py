Base = int(input("Enter the number of base:"))
Char = str(input("Enter the symbol you want:"))
for i in range(int((Base + 1) / 2 + 1)):
    print(
        int((Base - (2 * i - 1)) / 2) * " ",
        Char * (2 * i - 1),
        int((Base - (2 * i - 1)) / 2) * " ",
    )
