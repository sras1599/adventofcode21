from typing import List, Tuple

from parse_input import parse_input


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Instruction:
    def __init__(self, axis: str, count: int) -> None:
        self.axis = axis
        self.count = count


class TransparentPaper:
    def __init__(self, points: List[Tuple[int, int]], instructions: List[Tuple[str, int]]) -> None:
        self.points = [Point(x, y) for x, y in points]
        self.instructions = [Instruction(axis, count) for axis, count in instructions]

    def fold(self) -> None:
        for instruction in self.instructions:
            if instruction.axis == "x":
                self.fold_horizontally(instruction.count)
            elif instruction.axis == "y":
                self.fold_vertically(instruction.count)

    def fold_horizontally(self, by: int):
        points_to_fold = (point for point in self.points if point.x > by)

        for point in points_to_fold:
            point.x = by - (point.x - by)

    def fold_vertically(self, by: int):
        points_to_fold = (point for point in self.points if point.y > by)

        for point in points_to_fold:
            point.y = by - (point.y - by)

    def __str__(self) -> str:
        grid = [
            ["." for _ in range(max(self.points, key=lambda p: p.x).x + 1)]
            for _ in range(max(self.points, key=lambda p: p.y).y + 1)
        ]

        for point in self.points:
            grid[point.y][point.x] = "#"

        return "\n".join("".join(row) for row in grid)

    @property
    def height(self) -> int:
        return max(point.y for point in self.points)

    @property
    def width(self) -> int:
        return max(point.x for point in self.points)


def main():
    with open("input", "r") as file:
        points, instructions = parse_input(file)

    paper = TransparentPaper(points, instructions)

    paper.fold()
    print(paper)


if __name__ == "__main__":
    main()
