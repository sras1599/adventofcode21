from io import TextIOWrapper
from typing import List


def parse_input(file: TextIOWrapper):
    cavern: List[List[int]] = []

    for line in file:
        cavern.append([int(char) for char in list(line.strip())])

    return cavern
