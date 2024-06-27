import customtkinter as ctk
import random

# Global variables
window = None
current_player = "X"
board = [""] * 9
game_over = False
opponent = None
buttons = []
status_label = None

def create_widgets():
    global window, buttons, status_label

    window = ctk.CTk()
    window.title("Tic Tac Toe")
    window.geometry("400x450")

    opponent_frame = ctk.CTkFrame(window)
    opponent_frame.pack(pady=10)

    ai_button = ctk.CTkButton(opponent_frame, text="Play vs AI", command=lambda: set_opponent("AI"))
    ai_button.pack(side="left", padx=5)

    human_button = ctk.CTkButton(opponent_frame, text="Play vs Human", command=lambda: set_opponent("Human"))
    human_button.pack(side="left", padx=5)

    game_frame = ctk.CTkFrame(window)
    game_frame.pack(pady=10)

    for i in range(9):
        button = ctk.CTkButton(game_frame, text="", width=80, height=80, command=lambda x=i: make_move(x))
        button.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(button)

    status_label = ctk.CTkLabel(window, text="Select opponent to start")
    status_label.pack(pady=10)

    reset_button = ctk.CTkButton(window, text="Reset Game", command=reset_game)
    reset_button.pack(pady=10)

def set_opponent(chosen_opponent):
    global opponent
    opponent = chosen_opponent
    reset_game()
    status_label.configure(text=f"Playing against {opponent}. X's turn")

def make_move(position):
    global current_player, game_over

    if board[position] == "" and not game_over and opponent:
        board[position] = current_player
        buttons[position].configure(text=current_player)
        
        if check_winner():
            status_label.configure(text=f"{current_player} wins!")
            game_over = True
        elif "" not in board:
            status_label.configure(text="It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.configure(text=f"{current_player}'s turn")
            
            if opponent == "AI" and current_player == "O" and not game_over:
                ai_move()

def ai_move():
    available_moves = [i for i, spot in enumerate(board) if spot == ""]
    if available_moves:
        move = random.choice(available_moves)
        make_move(move)

def check_winner():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return True
    return False

def reset_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    for button in buttons:
        button.configure(text="")
    if opponent:
        status_label.configure(text=f"Playing against {opponent}. X's turn")
    else:
        status_label.configure(text="Select opponent to start")

# Create and run the game
create_widgets()
window.mainloop()