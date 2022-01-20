from io import TextIOWrapper
from typing import List, Tuple


def parse_input(file: TextIOWrapper) -> List[List[int]]:
    horizontal_lines = [[int(char) for char in line.strip()] for line in file]

    return horizontal_lines
