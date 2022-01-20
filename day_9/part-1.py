import math
from typing import List

from parse_input import parse_input


def pad_array(array: List[List[int]], pad=math.inf) -> List[List[int]]:
    return [[pad] * (len(array[0]) + 1)] + [[pad] + i + [pad] for i in array] + [[pad] * (len(array[0]) + 1)]


def find_low_points(array: List[List[int]]) -> List:
    low_points = []

    for i in range(1, len(array) - 1):
        for j in range(1, len(array[i]) - 1):
            point = array[i][j]

            prev_h, next_h = array[i][j - 1], array[i][j + 1]
            prev_v, next_v = array[i - 1][j], array[i + 1][j]

            if point < min(prev_h, next_h, prev_v, next_v):
                low_points.append(point + 1)

    return low_points


def main() -> None:
    with open("input", "r") as file:
        horizontal_lines = pad_array(parse_input(file))

    print(sum(find_low_points(horizontal_lines)))


if __name__ == "__main__":
    main()
