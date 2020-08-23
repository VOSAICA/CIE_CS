def output_space(i, x):
    print(int((x - (2 * i - 1)) / 2) * " ", end="")


def output_char(i, y):
    print(y * (2 * i - 1), end="")


def output_space_end(i, x):
    print(int((x - (2 * i - 1)) / 2) * " ")


def output(x, y):
    for i in range(1, int((x + 1) / 2) + 1):
        output_space(i, x)
        output_char(i, y)
        output_space_end(i, x)


def main():
    base = int(input("Enter the number of base:"))
    if base % 2 == 0:
        print("The base must be a odd!")
        main()
    char = str(input("Enter the symbol you want:"))
    output(base, char)


main()
