from __future__ import annotations

from typing import List

from a_star import Grid, a_star_search
from parse_input import parse_input


def main():
    with open("input", "r") as file:
        points: List[List[int]] = parse_input(file)

    cavern = Grid(points)

    cost = a_star_search(cavern)
    print(cost)


if __name__ == "__main__":
    main()
