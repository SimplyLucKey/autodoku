import pyautogui
import pprint

''' algorithm for solving sudoku
step 1: pick empty square
step 2: try all numbers that does not break the constraint
step 3: find a number that does not break the constraint
step 4: repeat step 1-3
step 5: backtrack
'''

''' example board
board = [[7, 8, 0,  4, 0, 0,  1, 2, 3]
         [6, 0, 0,  0, 7, 5,  0, 0, 9]
         [0, 0, 0,  6, 0, 1,  0, 7, 8]
         [0, 0, 7,  0, 4, 0,  2, 6, 0]
         [0, 0, 1,  0, 5, 0,  9, 3, 0]
         [9, 0, 4,  0, 6, 0,  0, 0, 5]
         [0, 7, 0,  3, 0, 0,  0, 1, 2]
         [1, 2, 0,  0, 0, 7,  4, 0, 0]
         [0, 4, 9,  2, 0, 6,  0, 0, 7]]
'''

''' sudoku website
www.sudoku.com
- input the puzzles and run
- sit back and watch the hardest puzzles get solved in less than a minute
'''

def input_puzzle():
    board = []

    for i in range(9):
        row = []

        # get user input until it's correct or done
        while True:
            try:
                x = input(f'Input row {i + 1}. Missing squares should be 0\n')

                # check for correct length of input
                if len(x) != 9:
                    raise Exception

                # check for only input digits
                else:
                    int(x)

                    for idx in range(9):
                        row.append(int(x[idx]))
                    break

            except Exception:
                print('Error. Try again. There should be 9 digits')

        board.append(row)
    return board


# function that selects an empty square, denoted by 0
def pick_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return row, col

    # todo for no more empty spaces
    return None, None

# function for checking the input if it's valid
def is_valid(board, guess, row, col):

    # check row validity first
    if guess in board[row]:
        return False

    # check col validity
    for i in range(9):
        if guess == board[i][col]:
            return False

    # check the inner square validity
    # get box labels
    box_r = row // 3 * 3 # 0 - 2 for box1, 3 - 5 for box2, 6 - 9 for box3
    box_c = col // 3 * 3

    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if guess == board[i][j]:
                return False

    return True


def solver(board):

    # find empty space
    row, col = pick_empty(board)

    if row is None:
        return True

    # guess from 1 through 9
    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess

            if solver(board):
                return True

        # backtracking
        board[row][col] = 0
    return False


def autofill(board):
    # locate first cell
    pyautogui.click(388, 262)

    # for mutation purposes
    dummy = board

    for row in range(len(dummy)):

        if row % 2 == 1:
            dummy[row].reverse()
            for col in range(len(dummy[row])):
                print(dummy[row][col])
                pyautogui.press(str(dummy[row][col]))
                pyautogui.press('left')

        elif row % 2 == 0:
            for col in range(len(dummy[row])):
                print(dummy[row][col])
                pyautogui.press(str(dummy[row][col]))
                pyautogui.press('right')

        pyautogui.press('down')


if __name__ == '__main__':
    board = input_puzzle()
    solver(board)
    autofill(board)
    # pprint.pprint(board)