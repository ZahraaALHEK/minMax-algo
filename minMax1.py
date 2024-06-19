import tkinter as tk
from tkinter import messagebox

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_winner(board):
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] != " ":
            return line[0]
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10
    elif winner == "O":
        return 10
    elif all(board[i][j] != " " for i in range(3) for j in range(3)):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    if score < best_score:
                        best_score = score
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.game_over = False
        self.board = initialize_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font=('Calibri', 40), height=1, width=3,
                            command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, i, j):
        if self.game_over or self.board[i][j] != " ":
            return
        self.board[i][j] = "X"
        self.buttons[i][j].config(text='X', disabledforeground='black')
        winner = check_winner(self.board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.game_over = True
            return
        if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.game_over = True
            return
        self.computer_move()

    def computer_move(self):
        move = find_best_move(self.board)
        if move:
            self.board[move[0]][move[1]] = "O"
            self.buttons[move[0]][move[1]].config(text='O', disabledforeground='black')
        winner = check_winner(self.board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.game_over = True
        elif all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.game_over = True

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
