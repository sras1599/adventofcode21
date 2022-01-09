from __future__ import annotations

from typing import List

from parse_input import parse_input

with open("input", "r") as file:
    numbers, grids = parse_input(file)


class RowOrColumn:
    def __init__(self, row: List[int], board: Board):
        self.row = row
        self.board = board

    def check(self, number: int) -> bool:
        return number in self.row

    def mark(self, number: int) -> None:
        if self.check(number):
            self.row.remove(number)

        if self.is_empty:
            self.board.won = True
            Bingo.WINNING_SCORES.append(self.board.get_score(number))

    def sum(self) -> int:
        return sum(self.row)

    @property
    def is_empty(self) -> bool:
        return len(self.row) == 0


class Board:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = [RowOrColumn(row, self) for row in self.grid]
        self.columns = [RowOrColumn([row[i] for row in self.grid], self) for i in range(5)]
        self.won = False

    def get_score(self, current_number: int) -> int:
        return sum(row.sum() for row in self.rows) * current_number

    def __str__(self) -> str:
        return "\n".join([" ".join([str(i) for i in row]) for row in self.grid])


class Bingo:
    IS_COMPLETED = False
    WINNING_SCORES = []

    def __init__(self, numbers: List, grids: List[Board]):
        self.numbers = numbers
        self.boards = [Board(grid) for grid in grids]

    def propagate(self, number: int) -> None:
        for board in self.playing_boards:
            for row in board.rows:
                row.mark(number)
            for column in board.columns:
                column.mark(number)

        if len(self.playing_boards) == 0:
            self.IS_COMPLETED = True

    def play(self) -> None:
        while not self.IS_COMPLETED:
            self.propagate(next(self.numbers))

    @property
    def winner(self) -> Board:
        return self.WINNING_SCORES.pop()

    @property
    def playing_boards(self):
        return [board for board in self.boards if not board.won]


if __name__ == "__main__":
    game = Bingo(numbers, grids)
    game.play()
    print(game.winner)
