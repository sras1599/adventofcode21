from io import TextIOWrapper
from itertools import chain
from typing import Dict, List


def parse_input(file: TextIOWrapper) -> List[Dict]:
    line_labels = ["x1", "y1", "x2", "y2"]
    lines = []

    for line in file:
        line = line.rstrip().split(" -> ")
        points = [int(point) for point in chain(*[segment.split(",") for segment in line])]

        lines.append(dict(zip(line_labels, points)))

    return lines
