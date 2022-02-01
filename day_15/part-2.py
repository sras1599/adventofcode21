from __future__ import annotations

from typing import List

from a_star import Grid, a_star_search
from parse_input import parse_input


def add_one_with_bounds(num: int):
    return num + 1 if not num == 9 else 1


def expand(arr: List[List[int]], width: int, height: 100) -> List[List[int]]:
    for _ in range(4):
        for row in range(len(arr)):
            elements_to_select = arr[row][-width:]
            extension = [add_one_with_bounds(element) for element in elements_to_select]
            arr[row].extend(extension)

    for _ in range(4):
        elements_to_select = arr[-height:]
        extension = [[add_one_with_bounds(element) for element in row] for row in elements_to_select]
        arr.extend(extension)

    return arr


def main():
    with open("input", "r") as file:
        points: List[List[int]] = parse_input(file)

    points = expand(points, width=len(points), height=len(points[0]))
    cavern = Grid(points)

    cost = a_star_search(cavern)
    print(cost)


if __name__ == "__main__":
    main()
