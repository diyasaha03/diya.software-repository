import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
import random

root = tk.Tk()
root.title("Sudoku Solver & Number Game")
root.geometry("500x550")


label = Label(root, text="Fill in the Sudoku numbers and click Solve")
label.grid(row=0, column=0, columnspan=9, padx=10, pady=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=1, column=0, columnspan=9, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=2, column=0, columnspan=9, pady=5)

cells = {}

def validate_number(p):
    return (p.isdigit() or p == "") and len(p) < 2

reg = root.register(validate_number)

def draw_3x3_grid(row, column, bg_color):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bg_color, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + j + 1, padx=1, pady=1, ipady=5)
            cells[(row + i, column + j)] = e

def draw_9x9_grid():
    color = "#D0ffff"
    for row_no in range(0, 9, 3):
        for col_no in range(0, 9, 3):
            draw_3x3_grid(row_no, col_no, color)
            color = "#ffffd0" if color == "#D0ffff" else "#D0ffff"

def clear_values():
    errLabel.config(text="")
    solvedLabel.config(text="")
    for cell in cells.values():
        cell.delete(0, tk.END)

def get_values():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = cells[(i, j)].get()
            if val == "":
                row.append(0)
            else:
                try:
                    num = int(val)
                    if 1 <= num <= 9:
                        row.append(num)
                    else:
                        messagebox.showerror("Input Error", "Please enter numbers from 1 to 9.")
                        return
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter valid numbers.")
                    return
        board.append(row)

    if solve_sudoku(board):
        update_cells(board)
        solvedLabel.config(text="Sudoku Solved!")
    else:
        errLabel.config(text="No solution exists for this Sudoku!")

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def update_cells(board):
    for row in range(9):
        for col in range(9):
            cells[(row, col)].delete(0, tk.END)
            if board[row][col] != 0:
                cells[(row, col)].insert(0, str(board[row][col]))

sample_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


guess_number = random.randint(1, 100)
remaining_attempts = 5

def check_guess():
    global remaining_attempts
    try:
        guess = int(guess_entry.get())
        if guess < guess_number:
            result_label.config(text=f"Try a higher number. {remaining_attempts} attempts left.")
        elif guess > guess_number:
            result_label.config(text=f"Try a lower number. {remaining_attempts} attempts left.")
        else:
            result_label.config(text=f"Congratulations! You guessed it right. The number was {guess_number}.")
            guess_btn.config(state=tk.DISABLED)
            guess_entry.config(state=tk.DISABLED)
        remaining_attempts -= 1
        if remaining_attempts == 0:
            result_label.config(text=f"Game over. The number was {guess_number}.")
            guess_btn.config(state=tk.DISABLED)
            guess_entry.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

number_game_label = Label(root, text="Number Guessing Game: Guess a number between 1 and 100.")
number_game_label.grid(row=18, column=0, columnspan=9, pady=10)

guess_label = Label(root, text="Enter your guess:")
guess_label.grid(row=19, column=0, columnspan=3)

guess_entry = Entry(root, width=10)
guess_entry.grid(row=19, column=3, columnspan=3, padx=10)

guess_btn = Button(root, text="Guess", command=check_guess)
guess_btn.grid(row=19, column=6, columnspan=3, padx=10)

result_label = Label(root, text="")
result_label.grid(row=20, column=0, columnspan=9, pady=5)


draw_9x9_grid()
update_cells(sample_board)


root.mainloop()