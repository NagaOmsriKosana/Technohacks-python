import tkinter as tk
from tkinter import messagebox
import random

# Initialize the game variables
current_player = "X"
board = [" " for _ in range(9)]

# Function to check for a win
def check_win():
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != " ":
            return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

# Function to handle player's move
def player_move(position):
    global current_player

    if board[position] == " ":
        board[position] = current_player
        update_button_text(position)
        
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                computer_move()

# Function to handle computer's move (random)
def computer_move():
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    move = random.choice(empty_cells)
    player_move(move)

# Function to update the button text on the GUI
def update_button_text(position):
    buttons[position].config(text=board[position], state="disabled")

# Function to reset the game board
def reset_board():
    global current_player, board
    current_player = "X"
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 20), width=5, height=2, command=lambda i=i: player_move(i))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

# Create a reset button
reset_button = tk.Button(root, text="Reset", command=reset_board)
reset_button.grid(row=3, column=1)

# Start the game
root.mainloop()
