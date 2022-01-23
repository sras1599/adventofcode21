from io import TextIOWrapper
from typing import List


def parse_input(file: TextIOWrapper):
    energy_levels: List[List[int]] = []

    for line in file:
        energy_levels.append([int(energy_level) for energy_level in list(line.strip())])

    return energy_levels
