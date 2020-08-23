def init_board():  # Create the board
    board = [[0 for col in range(10)] for row in range(9)]
    return board


def player1(b):  # Ask player 1 to input the row
    row = int(input("player1's turn: "))
    for i in range(8, 2, -1):
        if b[i][row - 1] == 0:
            b[i][row - 1] = 1
            break
        elif i == 3:
            print("All had been used, choose another row: ")
            player1(b)


def player2(b):  # Ask player 2 to input the row
    row = int(input("player2's turn: "))
    for i in range(8, 2, -1):
        if b[i][row - 1] == 0:
            b[i][row - 1] = 2
            break
        elif i == 3:
            print("All had been used")
            player2(b)


def display(b):  # Print the board after change
    for i in range(1, 8):
        print("(", i, ")", end="")
    print("\n")
    for i in range(3, 9):
        for j in range(0, 7):
            if b[i][j] == 0:
                print("|", " ", "|", end="")
            elif b[i][j] == 1:
                print("|", "O", "|", end="")
            elif b[i][j] == 2:
                print("|", "X", "|", end="")
            else:
                print("|", b[i][j], "|", end="")
        print("")


# You may write this part with DFS,
# but there is an old Chinese saying called: 杀鸡焉用牛刀
def win_horizon(b):
    for i in range(3, 9):
        for j in range(0, 7):
            if b[i][j] != 0:
                if b[i][j] == b[i][j + 1] == b[i][j + 2] == b[i][j + 3]:
                    return True
    return False


def win_vertical(b):
    for i in range(3, 6):
        for j in range(0, 7):
            if b[i][j] != 0:
                if b[i][j] == b[i + 1][j] == b[i + 2][j] == b[i + 3][j]:
                    return True
    return False


def win_oblique_negative(b):
    for i in range(3, 6):
        for j in range(0, 7):
            if b[i][j] != 0:
                if (
                    b[i][j]
                    == b[i + 1][j + 1]
                    == b[i + 2][j + 2]
                    == b[i + 3][j + 3]
                    != 0
                ):
                    return True
    return False


def win_oblique_positive(b):
    for i in range(6, 9):
        for j in range(0, 7):
            if b[i][j] != 0:
                if (
                    b[i][j]
                    == b[i - 1][j + 1]
                    == b[i - 2][j + 2]
                    == b[i - 3][j + 3]
                    != 0
                ):
                    return True
    return False


def diagnose(b):  # Detect is there anyone win for one method
    if (
        win_vertical(b)
        or win_horizon(b)
        or win_oblique_positive(b)
        or win_oblique_negative(b)
    ):
        return True
    return False


def start_game():
    board = init_board()
    display(board)
    while True:
        player1(board)
        display(board)
        if diagnose(board):
            print("player1 won!!!")
            break
        player2(board)
        display(board)
        if diagnose(board):
            print("player2 won!!!")
            break


start_game()
