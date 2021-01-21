#!/usr/bin/env python3

import sys
import chess.pgn
from chess.engine import PovScore, Cp


class Puzzle:
    def __init__(self, fen: str, badmove: str, better_moves: list):
        self.fen = fen
        self.badmove = badmove
        self.better_moves = better_moves

    @property
    def analysis_link(self):
        return f"https://www.chess.com/analysis?fen={self.fen}"

    def pretty_print(self):
        print(f"FEN: {self.fen}")
        print(f"Link: {self.analysis_link}")
        print(f"Bad Move: {self.badmove}")
        print(f"Better Moves: {self.better_moves}\n\n")

    def __repr__(self):
        return f"Puzzle: {self.fen}"

    def __str__(self):
        return f"Puzzle: {self.fen}"


class GameEngine:

    # TODO make this configurable.
    ENGINE_PATH = "/usr/bin/stockfish"

    def __init__(self, player: str, game_path: str):
        self.player = player
        self.game_path = game_path
        self.engine = chess.engine.SimpleEngine.popen_uci(self.ENGINE_PATH)
        self.color = chess.WHITE
        self.blunder_threshold = 100
        self.engine_time_limit = 1

        with open(game_path) as f:
            self.game = chess.pgn.read_game(f)
            self.board = self.game.board()

        if player == self.game.headers["Black"]:
            self.color = chess.BLACK

    def find_puzzles(self):
        node = self.game
        previous_result = None

        while not node.is_end():
            next_node = node.variation(0)
            self.board.push(next_node.move)
            fen = None
            if node.parent:
                fen = node.parent.board().fen()

            result = self.engine.analyse(
                node.board(), chess.engine.Limit(time=self.engine_time_limit)
            )

            if previous_result:
                before = previous_result["score"]
            else:
                before = PovScore(Cp(0), chess.WHITE)

            delta = (
                before.pov(self.color).score() - result["score"].pov(self.color).score()
            )
            if delta > self.blunder_threshold:
                badmove = node.parent.board().san(node.move)
                better_moves = [m.uci() for m in previous_result["pv"]]
                yield Puzzle(fen, badmove, better_moves)

            node = next_node
            previous_result = result

        self.engine.close()

    def __repr__(self):
        return f"Game: {self.game_path}"

    def __str__(self):
        return f"Game: {self.game_path}"


if __name__ == "__main__":
    player, pgn = sys.argv[1:]
    ge = GameEngine(player, pgn)
    for puzzle in ge.find_puzzles():
        puzzle.pretty_print()
