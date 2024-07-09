import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.chances = 5
        self.random_number = random.randint(0, 100)

        tk.Label(master, text="Guess the number between 0 and 100:").pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        tk.Button(master, text="Guess", command=self.guess_number).pack()
        tk.Button(master, text="Reset", command=self.reset_game).pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def guess_number(self):
        try:
            user_guess = int(self.entry.get())
            if user_guess == self.random_number:
                self.end_game("You are right!")
            else:
                self.chances -= 1
                hint = "greater" if user_guess > self.random_number else "lesser"
                self.result_label.config(text=f"Your number is {hint} than the real number. {self.chances} chances left!")
                if self.chances == 0:
                    self.end_game(f"You've run out of chances! The number was {self.random_number}.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")

    def reset_game(self):
        self.chances = 5
        self.random_number = random.randint(0, 100)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

    def end_game(self, message):
        messagebox.showinfo("Result", message)
        self.reset_game()

root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()