# -*- coding: utf-8 -*-
import time
from breakthroughgame import BreakthroughGame
import pygame
import sys

# Like disabling the pygame screen stuff, since we are not like displaying anything for these tests
pygame.display.set_mode = lambda size: pygame.Surface(size)
pygame.display.flip = lambda: None
pygame.display.set_caption = lambda title: None

class MatchRunner:
    def __init__(self):
        # This is like where we put all the matchups mentioned in the assignment
        self.matchups = [
            ("Minimax(Off1) vs AlphaBeta(Off1)", "minimax", 1, "alphabeta", 1),
            ("AlphaBeta(Off2) vs AlphaBeta(Def1)", "alphabeta", 7, "alphabeta", 2),
            ("AlphaBeta(Def2) vs AlphaBeta(Off1)", "alphabeta", 8, "alphabeta", 1),
            ("AlphaBeta(Off2) vs AlphaBeta(Off1)", "alphabeta", 7, "alphabeta", 1),
            ("AlphaBeta(Def2) vs AlphaBeta(Def1)", "alphabeta", 8, "alphabeta", 2),
            ("AlphaBeta(Off2) vs AlphaBeta(Def2)", "alphabeta", 7, "alphabeta", 8),
        ]
        self.results = []  # Like just saving all the results from each match here

    def run_game(self, black_type, black_func, white_type, white_func):
        # This is for starting a new game instance and setting it to auto mode
        game = BreakthroughGame()
        game.status = 5  # setting the status to 5 so the AIs can like auto play

        while game.status != 3:
            game.clock.tick(60)
            game.screen.fill([255, 255, 255])  # just clearing the screen

            start = time.process_time()  # This is like starting a stopwatch

            if game.turn == 1:
                if black_type == "minimax":
                    game.ai_move_minimax(black_func)  # Black playing
                else:
                    game.ai_move_alphabeta(black_func)
                game.total_time_1 += time.process_time() - start
                game.total_step_1 += 1
            else:
                if white_type == "minimax":
                    game.ai_move_minimax(white_func)  # White playing
                else:
                    game.ai_move_alphabeta(white_func)
                game.total_time_2 += time.process_time() - start
                game.total_step_2 += 1

            game.display()  # Even if we don’t really see it, we keep it here

        # This is for deciding the winner based on breakthrough rules
        if any(cell == 2 for cell in game.boardmatrix[0]):
            winner = "White"  # White reached top row
        elif any(cell == 1 for cell in game.boardmatrix[7]):
            winner = "Black"  # Black reached bottom row
        else:
            # fallback — all opponent pieces captured
            black_count = sum(row.count(1) for row in game.boardmatrix)
            white_count = sum(row.count(2) for row in game.boardmatrix)
            winner = "White" if black_count == 0 else "Black"

        return {
            "winner": winner,
            "final_board": game.boardmatrix,
            "total_nodes_1": game.total_nodes_1,
            "total_nodes_2": game.total_nodes_2,
            "avg_nodes_1": game.total_nodes_1 / game.total_step_1 if game.total_step_1 else 0,
            "avg_nodes_2": game.total_nodes_2 / game.total_step_2 if game.total_step_2 else 0,
            "avg_time_1": game.total_time_1 / game.total_step_1 if game.total_step_1 else 0,
            "avg_time_2": game.total_time_2 / game.total_step_2 if game.total_step_2 else 0,
            "pieces_captured_by_1": 16 - sum(row.count(2) for row in game.boardmatrix),
            "pieces_captured_by_2": 16 - sum(row.count(1) for row in game.boardmatrix),
            "total_moves_1": game.total_step_1,
            "total_moves_2": game.total_step_2,
        }

    def run_all(self):
        # This is for going through every matchup and running it one by one
        for label, black_type, black_func, white_type, white_func in self.matchups:
            print(f"Running matchup: {label}")  # This is just like printing what we're doing
            result = self.run_game(black_type, black_func, white_type, white_func)  # running the actual match
            self.results.append((label, result))  # saving the result for later

    def save_results(self, filename="match_results.txt"):
        # This is for saving everything to a text file to make reporting easier later
        with open(filename, "w", encoding="utf-8") as f:
            for label, result in self.results:
                f.write(f"=== {label} ===\n")
                f.write(f"Winner: {result['winner']}\n")
                f.write("Final Board State:\n")
                for row in result["final_board"]:
                    f.write(" ".join(map(str, row)) + "\n")
                f.write(f"Total nodes (Black): {result['total_nodes_1']}\n")
                f.write(f"Total nodes (White): {result['total_nodes_2']}\n")
                f.write(f"Avg nodes/move (Black): {result['avg_nodes_1']:.2f}\n")
                f.write(f"Avg nodes/move (White): {result['avg_nodes_2']:.2f}\n")
                f.write(f"Avg time/move (Black): {result['avg_time_1']:.4f} sec\n")
                f.write(f"Avg time/move (White): {result['avg_time_2']:.4f} sec\n")
                f.write(f"Captured by Black: {result['pieces_captured_by_1']}\n")
                f.write(f"Captured by White: {result['pieces_captured_by_2']}\n")
                f.write(f"Total moves (Black): {result['total_moves_1']}\n")
                f.write(f"Total moves (White): {result['total_moves_2']}\n")
                f.write("\n")

# This is for calling the match runner and running all the matches when the file is executed
if __name__ == "__main__":
    runner = MatchRunner()
    runner.run_all()
    runner.save_results()
