from io import TextIOWrapper
from typing import List


def parse_input(file: TextIOWrapper):
    points: List[List[str]] = []

    for line in file:
        points.append(line.strip().split("-"))

    return points
