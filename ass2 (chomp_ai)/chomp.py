import copy
import time

Rows = 0
Cols = 0


def play_again():
    print("play again?")
    return input().lower().startswith("y")


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end="  ")
        print()


def validate_user_input(player_choice, board):
    try:
        row, col = player_choice.split()
    except ValueError:
        print("Bad input: The input should be exactly two numbers separated by a space.")
        return False
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("Input must be two numbers, however non-digit characters were received.")
        return False

    if row < 0 or row > Rows - 1:
        print(f"The first number must be between 0 and {Rows - 1} but {row} was passed.")
        return False
    if col < 0 or col > Cols - 1:
        print(f"The second number must be between 0 and {Cols - 1} but {col} was passed.")
        return False
    if board[row][col] == " ":
        print("That square has already been eaten!")
        return False
    return True


def update_board(board, row, col):
    for i in range(row, -1, -1):
        for j in range(col, len(board[i])):
            board[i][j] = " "


def get_human_move(board):
    valid_input = False
    while not valid_input:
        player_choice = input("Enter the row and column of your choice separated by a space: ")
        valid_input = validate_user_input(player_choice, board)
    row, col = player_choice.split()
    return int(row), int(col)


def check_win(board, computer):  # evaluation function

    for x in range(Rows):
        for y in range(Cols):
            if board[x][y] == '*':
                return 0

    if computer:
        return 1
    else:
        return -1


def minmax(board, maximizing):
    if check_win(board, True) == 1:
        return 1
    if check_win(board, False) == -1:
        return -1

    if maximizing:
        best_score = -100

        for x in range(Rows):
            for y in range(Cols):
                if board[x][y] == '*':
                    copy_board = copy.deepcopy(board)
                    update_board(copy_board, x, y)

                    score = minmax(copy_board, False)
                    if score > best_score:
                        best_score = score

        return best_score

    else:
        best_score = 100

        for x in range(Rows):
            for y in range(Cols):
                if board[x][y] == '*':
                    copy_board = copy.deepcopy(board)
                    update_board(copy_board, x, y)

                    score = minmax(copy_board, False)
                    if score < best_score:
                        best_score = score

        return best_score


def get_computer_move(board):
    best_score = -100
    best_row = 0
    best_col = 0

    for x in range(Rows):
        for y in range(Cols):
            if board[x][y] == '*':
                copy_board = copy.deepcopy(board)
                update_board(copy_board, x, y)

                score = minmax(copy_board, False)
                if score > best_score:
                    best_score = score
                    best_row = x
                    best_col = y

    return best_row, best_col


def main():
    global Rows
    global Cols
    valid_input = False

    Rows = int(input("Enter number of rows : "))
    Cols = int(input("Enter number of columns : "))
    while not valid_input:
        if Rows <= 0 or Cols <= 0:
            print("!.....Bad input....!")
            Rows = int(input("Enter number of rows : "))
            Cols = int(input("Enter number of columns : "))
        else:
            valid_input = True

    board = []
    for i in range(Rows):
        row = []
        for j in range(Cols):
            row.append("*")
        board.append(row)

    board[Rows - 1][0] = "P"
    game = True
    turn = True  # True for human false for computer

    while game:
        if turn:
            if check_win(board, True) == 1:
                print()
                print("Too bad, the computer wins!")
                game = False
                break
            print("Players turn.")
            print()
            print_matrix(board)
            print()

            row, col = get_human_move(board)

            if board[row][col] == "P":
                print()
                print("Too bad, the computer wins!")
                game = False

            else:
                update_board(board, row, col)
                print()
                print_matrix(board)
                print()
                time.sleep(1)
                turn = False

        else:

            if check_win(board, False) == -1:
                print()
                print("you win!")
                game = False
            row, col = get_computer_move(board)
            print(f"Computer turn. the computer chooses ({row}, {col})")
            print()

            update_board(board, row, col)
            print_matrix(board)
            print()
            time.sleep(1)
            turn = True

    if play_again():
        main()
    else:
        return 0


main()
