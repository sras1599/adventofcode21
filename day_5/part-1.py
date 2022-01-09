from __future__ import annotations

from collections import Counter
from itertools import zip_longest
from typing import Generator, List, Tuple

from parse_input import parse_input


class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def is_eligible(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def points_covered(self) -> Generator[Tuple[int, int], None, None]:
        x_step = 1 if self.x1 <= self.x2 else -1
        y_step = 1 if self.y1 <= self.y2 else -1
        fillvalue = self.x1 if self.x1 == self.x2 else self.y1

        points = zip_longest(
            range(self.x1, self.x2 + x_step, x_step), range(self.y1, self.y2 + y_step, y_step), fillvalue=fillvalue
        )

        yield from points

    def __str__(self) -> str:
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"


class Graph:
    def __init__(self, lines: List[Line]) -> None:
        self.lines = [line for line in lines if line.is_eligible]

    def get_number_of_overlapped_points(self) -> int:
        counter = Counter(self.points_covered())

        return len([freq for freq in counter.values() if freq >= 2])

    def points_covered(self) -> Generator[Tuple[int, int], None, None]:
        for line in self.lines:
            yield from line.points_covered()


def main():
    with open("input", "r") as file:
        lines = parse_input(file)

    lines = [Line(**line) for line in lines]
    graph = Graph(lines)

    print(graph.get_number_of_overlapped_points())


if __name__ == "__main__":
    main()
