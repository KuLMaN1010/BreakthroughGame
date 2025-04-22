Breakthrough Game - CSC 412 Assignment 2  
===========================================

This is my implementation of the Breakthrough Game AI project. 
The project includes both a graphical user interface (GUI) to play or test the game, 
and an automated script to run all the matchups for evaluation. 
I’ve listed the steps below to run everything properly.

Software Requirements: 
• Python 3.9+  
• Pygame (used for GUI)  
• Visual Studio 2022 (what I used, but any IDE should work honestly)  
• NumPy (some parts of the AI logic use this)

How to Install Dependencies:
Open terminal / cmd and run: pip install pygame numpy

Project Files Explained:
• `breakthroughgame.py` → This is the GUI file. Run this to play manually or see the game visually.  
• `match_runner.py` → This is the script for running all 6 required matchups. It does NOT show the GUI.  
• `model.py` → This contains the State class, heuristics, utility functions, and board logic.  
• `minimax_agent.py` → The AI agent using plain minimax (used in matchup 1).  
• `alpha_beta_agent.py` → The smarter AI agent using alpha-beta pruning.  
• `src/` folder → This has all the images used by the GUI (pieces, board, icons, etc).
[Add all this in there and then you are good]

How to Run the Project: 
1. Open the solution/project folder in Visual Studio 2022 or any editor.
2. If you want to run the actual GUI game and like manually play or test some heuristics yourself, run: breakthroughgame.py as the startup file
- This will open a window and you’ll see the board.
- Click on the pieces to move manually.
- You can also click the computer icon to make a single AI move.
- And clicking AUTO lets the AIs play continuously with hardcoded heuristics (editable in the code if needed).

3. If you want to run all the required matchups (like for the report), just run: match_runner.py as the startup file- It doesn’t show the GUI or anything visual, it just quietly runs everything.
- A file called `match_results.txt` will be created in the folder.
- This contains all the match results with stats like winner, final board state, captured pieces, avg time/nodes per move, and total moves.

About the AI  
• Minimax search goes to a depth of 3.  
• Alpha-beta pruning search goes deeper than that[5].  
• Includes multiple heuristics:
- Offensive Heuristic 1
- Defensive Heuristic 1
- Offensive Heuristic 2 (I designed this to beat Def1)
- Defensive Heuristic 2 (I designed this to beat Off1)

GitHub Link    
If you'd like to try the GitHub version instead or want to take a look there, feel free to email me and I’ll share the link with you privately! :)

Thanks for checking it out!!


