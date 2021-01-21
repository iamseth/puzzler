# puzzler

Quick script to read in a Chess PGN file and find blunders during the game.

If a blunder is detected, the position, the bad move that was made during the game, and the engine's list of better moves are given.

Additionally, a link to an analysis board on Chess.com is provided. Maybe I'll make my own UI at some point using https://chessboardjs.com


## Example

Running against the sample PGN as my username.

```bash
> ./puzzler.py iamsethmiller ./data/sample.pgn 

FEN: 2kr3r/b1p2pp1/P1ppb1qp/4p3/P3P3/3P3P/2PQNPPK/RN3R2 b - - 0 16
Link: https://www.chess.com/analysis?fen=2kr3r/b1p2pp1/P1ppb1qp/4p3/P3P3/3P3P/2PQNPPK/RN3R2 b - - 0 16
Bad Move: c5
Better Moves: ['c8d7', 'a4a5', 'g6f6', 'b1c3', 'g7g5', 'a1b1', 'd8a8', 'c3a4', 'h8b8', 'b1b7', 'd7c8', 'd2c3', 'e6d7', 'f1b1', 'f6f2', 'e2g3', 'f2d4', 'g3f5', 'd4c3', 'a4c3', 'd7e6', 'f5e7', 'c8d7', 'b7a7', 'a8a7', 'b1b8', 'd7e7']

FEN: 2kr3r/b4pp1/P1ppb1qp/P1p1p3/4P3/2NP3P/2PQNPPK/R4R2 b - - 0 18
Link: https://www.chess.com/analysis?fen=2kr3r/b4pp1/P1ppb1qp/P1p1p3/4P3/2NP3P/2PQNPPK/R4R2 b - - 0 18
Bad Move: d5
Better Moves: ['c8c7', 'f2f4']

FEN: 2kr3r/b4pp1/P1p1b1qp/P1pPp3/8/2NP3P/2PQNPPK/R4R2 b - - 0 19
Link: https://www.chess.com/analysis?fen=2kr3r/b4pp1/P1p1b1qp/P1pPp3/8/2NP3P/2PQNPPK/R4R2 b - - 0 19
Bad Move: cxd5
Better Moves: ['e6d5', 'e2g3', 'h6h5', 'a1b1', 'd8d7', 'd2e1', 'h5h4', 'g3e4', 'f7f5', 'c3d5', 'c6d5', 'e4c3', 'e5e4', 'c3a4', 'g6d6', 'h2g1', 'd6a6', 'a4b6', 'a7b6', 'b1b6', 'h8h6', 'b6a6', 'h6a6', 'e1c3']

FEN: 2kr3r/b4pp1/P3b1qp/PNppp3/8/3P3P/2PQNPPK/R4R2 b - - 1 20
Link: https://www.chess.com/analysis?fen=2kr3r/b4pp1/P3b1qp/PNppp3/8/3P3P/2PQNPPK/R4R2 b - - 1 20
Bad Move: Bb8
Better Moves: ['d8d7']

```
