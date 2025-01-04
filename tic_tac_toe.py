import os
import random
from statistics import mode
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to print the Tic-Tac-Toe board with colors
def print_board(board):
    print(Fore.YELLOW + "\nCurrent Board:")
    for i in range(3):
        row = " | ".join([Fore.GREEN + cell if cell == ' ' else Fore.RED + cell for cell in board[i]])
        print(row)
        if i < 2:
            print(Fore.YELLOW + "---+---+---")
    print("\n")

# Function to check if there's a winner
def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Save the game state to a file
def save_game(board, current_player):
    with open('game_state.txt', 'w') as file:
        for row in board:
            file.write(','.join(row) + '\n')
        file.write(f"Player Turn: {current_player}\n")
    print("Game state saved!")

# Load the game state from a file
def load_game():
    if os.path.exists('game_state.txt'):
        with open('game_state.txt', 'r') as file:
            board = [line.strip().split(',') for line in file.readlines()[:3]]
            current_player = file.readline().strip().split(': ')[1]
            return board, current_player
    return None, None

# Get a valid move from the player
def get_move(board, current_player):
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1  # 1-index to 0-index
            row, col = divmod(move, 3)  # Convert 1D index to 2D coordinates (row, col)
            if 0 <= move < 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move or space taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# AI: Minimax Algorithm
def minimax(board, depth, is_maximizing, alpha, beta, depth_limit):
    if depth >= depth_limit:
        return 0  # Neutral evaluation

    if check_winner(board, 'O'):
        return 10 - depth  # AI wins
    if check_winner(board, 'X'):
        return depth - 10  # Player wins
    if board_full(board):
        return 0  # Draw

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # AI's move
                    eval = minimax(board, depth + 1, False, alpha, beta, depth_limit)
                    board[i][j] = ' '  # Undo move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Player's move
                    eval = minimax(board, depth + 1, True, alpha, beta, depth_limit)
                    board[i][j] = ' '  # Undo move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI Move (using Minimax)
def ai_move(board, difficulty):
    best_move = None
    best_value = float('-inf')
    depth_limit = 3 if difficulty == 'hard' else 2 if difficulty == 'medium' else 1

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI move
                move_value = minimax(board, 0, False, float('-inf'), float('inf'), depth_limit)
                board[i][j] = ' '  # Undo move

                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

# Function to display player stats
def display_stats(wins_x, wins_o, draws):
    print(Fore.CYAN + "\nGame Stats:")
    print(f"Player X Wins: {wins_x}")
    print(f"Player O Wins: {wins_o}")
    print(f"Draws: {draws}")

# Function to get player profile (Name)
def get_player_profile():
    name = input("Enter your player name: ").strip()
    return name

def save_profile(name, wins_x, wins_o, draws):
    with open(f"{name}_profile.txt", 'w') as f:
        f.write(f"Player: {name}\n")
        f.write(f"Wins: {wins_x}\n")
        f.write(f"Losses: {wins_o}\n")
        f.write(f"Draws: {draws}\n")
    print("Profile saved successfully!")

def load_profile(name):
    try:
        with open(f"{name}_profile.txt", 'r') as f:
            profile = f.readlines()
        print("Profile loaded:")
        for line in profile:
            print(line.strip())
    except FileNotFoundError:
        print("Profile not found, creating a new one.")
        return None
    
def play_again():
    while True:
        choice = input(Fore.GREEN + "Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("Thanks for playing! Goodbye.")
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'.")

# Main function to run the game
def tic_tac_toe():
    print(Fore.MAGENTA + "Welcome to Tic-Tac-Toe!")
    print("1. Start New Game")
    print("2. Load Saved Game")
    print("3. Quit")

    while True:
        try:
            choice = int(input("Choose an option (1-3): "))
            if choice == 1:
                game_choice = "new"
                break
            elif choice == 2:
                game_choice = "load"
                break
            elif choice == 3:
                print("Thank you for playing! Goodbye.")
                return
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1-3).")

    player_name = get_player_profile()

    mode = input("Do you want to play against (1) Player or (2) AI? Enter 1 or 2: ").strip()

    if game_choice == "load":
        board, current_player = load_game()
        if board is None:
            print("No saved game found. Starting a new game.")
            board = [[' ' for _ in range(3)] for _ in range(3)]
            current_player = '1'
    else:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = '1'

    wins_x, wins_o, draws = 0, 0, 0
    history = []

    if mode == '2':
        difficulty = input("Choose AI Difficulty (easy, medium, hard): ").strip().lower()

    while True:
        display_stats(wins_x, wins_o, draws)
        print_board(board)

        if mode == '1':  # Player vs Player
            print(f"Player {current_player}'s turn.")
            row, col = get_move(board, current_player)
            history.append([row[:] for row in board])
            board[row][col] = 'X' if current_player == '1' else 'O'

        elif mode == '2' and current_player == '1':  # Player vs AI, Player's turn
            print(f"Player {current_player}'s turn.")
            row, col = get_move(board, current_player)
            history.append([row[:] for row in board])
            board[row][col] = 'X'

        elif mode == '2' and current_player == '2':  # AI's turn
            print("AI is making its move...")
            row, col = ai_move(board, difficulty)
            board[row][col] = 'O'

        if check_winner(board, 'X' if current_player == '1' else 'O'):
            print_board(board)
            print(f"Player {current_player} wins!")
            if current_player == '1':
                wins_x += 1
            else:
                wins_o += 1
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            draws += 1
            break

        current_player = '2' if current_player == '1' else '1'

    save_choice = input("Do you want to save the game? (y/n): ").lower()
    if save_choice == 'y':
        save_game(board, current_player)

    save_profile(player_name, wins_x, wins_o, draws)

    if not play_again():
        return

if __name__ == "__main__":
    tic_tac_toe()


