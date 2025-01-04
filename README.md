# Masai-project
**Project Description:**
This project implements a console-based Tic-Tac-Toe game with several enhancements, such as the ability to play against either another player or an AI, save and load game states, and manage player profiles with statistics tracking.

The game is built in Python and uses the colorama library for colorful terminal output, creating a more engaging experience. The project also includes AI functionality, where the AI uses the minimax algorithm with alpha-beta pruning to make its moves, which adjusts based on the difficulty setting (easy, medium, or hard). Players can save their progress and come back to continue from where they left off, while player statistics (wins, losses, and draws) are tracked and saved in a player profile.
**Features Implemented:**
Tic-Tac-Toe Game Logic:

1. Players take turns placing their mark on a 3x3 grid.
   The game checks for a winner after every move.
    It also checks for a draw when the board is full but no winner is determined.
2. Player vs Player Mode:
   Two players can play locally, taking turns to place their 'X' and 'O' marks on the board.
3. Player vs AI Mode:
   Players can choose to play against the AI.
   The AI makes its moves using the Minimax algorithm, which determines the optimal move for the AI based on the current game 
    state. The AI difficulty can be set to easy, medium, or hard.
4. Save and Load Game States:
   Players can save their current game state to a file (game_state.txt) and load it back later to continue from where they left 
  off.
5. Profile Management:
   Each player can create and save a profile, tracking their wins, losses, and draws.
   The profile is saved in a text file with the player's name, and the statistics are updated after each game.
6. Game Stats Display:
   At any point, players can view their stats (wins, losses, draws) during the game.
7.Colored Terminal Output:
  The game uses **colorama** for coloring the board, game text, and player input, enhancing the user experience.
8. Replay Option:
  After each game, players are prompted to play again or exit.
**How to Run the Project:**
_Dependencies:
_
This project requires Python 3.x and the colorama library for colored output. Install colorama via pip:
pip install colorama
**Game Flow**:
Upon starting, you'll be prompted to choose one of the following options:

1.Start a new game
2.Load a saved game (if available)
3.Quit the game
You'll then be asked for your player name and to choose between playing against another player or the AI.

If playing against the AI, you will be prompted to select the difficulty level (easy, medium, or hard).

You will then take turns making moves by entering numbers between 1 and 9, corresponding to positions on the Tic-Tac-Toe board.

Example board:
diff
Copy code
1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
7 | 8 | 9
After every move, the board will be updated, and the game will check if there is a winner, a draw, or if the game should continue.

At the end of the game, the current player stats are displayed, and you can choose to save the game, save your profile, or play again.

**Commands:**
Save Game: After the game ends, you'll be prompted if you want to save the game state for later.
Save Profile: Your player profile (name, wins, losses, draws) will be saved in a file named <player_name>_profile.txt.
Load Saved Game: If you choose to load a saved game, the game state will be restored, and you can continue from where you left off.
Exiting:
The game will exit once you choose not to play again after a round, or if you select the quit option from the main menu.
**EXAMPLE**
Welcome to Tic-Tac-Toe!
1. Start New Game
2. Load Saved Game
3. Quit
Choose an option (1-3): 1
Enter your player name: Alice
Do you want to play against (1) Player or (2) AI? Enter 1 or 2: 2
Choose AI Difficulty (easy, medium, hard): medium
Game Stats:
Player X Wins: 0
Player O Wins: 0
Draws: 0

Current Board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player 1's turn.
Player 1, enter your move (1-9): 1

Current Board:
 X | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

...
Conclusion:
This project implements a full-featured Tic-Tac-Toe game with multiple playing modes, AI difficulty options, and player profile management. It offers an engaging experience for both casual play and strategic gameplay with the AI.
