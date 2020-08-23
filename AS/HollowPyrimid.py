def output_space(i, x):
    print(int((x - (2 * i - 1)) / 2) * " ", end='')


def output_inner(i):
    print((i * 2 - 3) * " ", end='')


def output_char(y):
    print(y, end='')


def output_space_end(i, x):
    print(int((x - (2 * i - 1)) / 2) * " ")


def output_end(x, y):
    print(y * x)


def output(x, y):
    output_space(1, x)
    output_char(y)
    output_space_end(1, x)
    for i in range(2, int((x + 1) / 2) ):
        output_space(i, x)
        output_char(y)
        output_inner(i)
        output_char(y)
        output_space_end(i, x)
    output_end(x, y)


def main():
    base = int(input("Enter the number of base:"))
    if base % 2 == 0:
        print("The base must be a odd!")
        main()
    char = str(input("Enter the symbol you want:"))
    output(base, char)


main()
