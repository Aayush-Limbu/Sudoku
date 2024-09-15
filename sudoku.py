import random
import copy
import sys

class SudokuGame:
    def __init__(self):
        self.board = self.generate_sudoku()
        self.solved_board = None

    def generate_sudoku(self):
        return [[0] * 9 for _ in range(9)]

    def print_sudoku(self, board):
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row_to_print = ""
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_to_print += "| "
                row_to_print += str(cell) if cell != 0 else '.'
                row_to_print += " "
            print(row_to_print)

    def solve_sudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    fill = list(range(1,10))
                    random.shuffle(fill)
                    for num in fill:
                        if self.check(board, i, j, num):
                            board[i][j] = num
                            if self.solve_sudoku(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    def check(self, board, row, column, num):
        return self.check_row(board, row, num) and self.check_column(board, column, num) and self.check_box(board, row, column, num)

    def check_row(self, board, row, num):
        return num not in board[row]

    def check_column(self, board, column, num):
        return all(board[i][column] != num for i in range(9))

    def check_box(self, board, row, column, num):
        start_row = (row // 3) * 3
        start_column = (column // 3) * 3
        return all(board[start_row + i][start_column + j] != num for i in range(3) for j in range(3))

    def hollow_out(self, filled_spots):
        total = 81
        hollow = total - filled_spots
        while hollow > 0:
            row, column = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][column] != 0:
                self.board[row][column] = 0
                hollow -= 1

    def user_input(self):
        valid_input = str(list(range(1, 10)))
        while self.board != self.solved_board:
            row = input("Please enter the row number: ")
            if row == 'q':
                print("Better luck next time.\nThe puzzle was: ")
                self.print_sudoku(self.solved_board)
                return False
            if not row in valid_input:
                print("Please enter a valid row number")
                continue
            
            column = input("Please enter the column number: ")
            if column == 'q':
                print("Better luck next time.\nThe puzzle was: ")
                self.print_sudoku(self.solved_board)
                return False
            if not column in valid_input:
                print("Please enter a valid column number")
                continue

            num = input("Please enter the input number: ") 
            if num == 'q':
                print("Better luck next time.\nThe puzzle was: ")
                self.print_sudoku(self.solved_board)
                return False
            if not num in valid_input:
                print("Please enter a valid number")
                continue

            row, column, num = int(row) - 1, int(column) - 1, int(num)
            if self.solved_board[row][column] == num:
                print("Correct input.")
                self.board[row][column] = num
                self.print_sudoku(game.board)
            else:
                print("Wrong input. Please try again.")
    
        print("Congratulations! You solved the puzzle.")
        return True

    def difficulty(self):
        difficulty_value = input("Select difficulty level:\nEasy (e)\nMedium (m)\nHard (h)\nPress 'q' at any time to quit.\n")
        if difficulty_value == 'e':
            return random.randint(36, 49)
        elif difficulty_value == 'm':
            return random.randint(32, 35)
        elif difficulty_value == 'h':
            return random.randint(28, 31)
        elif difficulty_value == 'q':
            print("Exiting the game. Better luck next time.")
            sys.exit()
        else:
            print("Please write a valid difficulty value.")
            return self.difficulty()

# Game Initialization
game = SudokuGame()
game.solve_sudoku(game.board)
game.solved_board = copy.deepcopy(game.board)
game.hollow_out(game.difficulty())
game.print_sudoku(game.board)
game.user_input()
