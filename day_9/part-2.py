import math
from functools import reduce
from operator import mul
from typing import List

from parse_input import parse_input


def pad_array(array: List[List[int]], pad=math.inf) -> List[List[int]]:
    return [[pad] * (len(array[0]) + 1)] + [[pad] + i + [pad] for i in array] + [[pad] * (len(array[0]) + 1)]


def find_coordinates_of_low_points(array: List[List[int]]) -> List:
    low_points = []

    for i in range(1, len(array) - 1):
        for j in range(1, len(array[i]) - 1):
            point = array[i][j]

            prev_h, next_h = array[i][j - 1], array[i][j + 1]
            prev_v, next_v = array[i - 1][j], array[i + 1][j]

            if point < min(prev_h, next_h, prev_v, next_v):
                low_points.append((i, j))

    return low_points


def get_points_in_basin(point: tuple, array: List[List[int]]) -> set:
    def traverse(point):
        i, j = point
        value = array[i][j]

        candidate_points = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))

        for point in candidate_points:
            point_value = array[point[0]][point[1]]

            if point_value < value or point_value in [math.inf, 9] or point in points_in_basin:
                continue
            else:
                points_in_basin.add(point)
                traverse(point)

    points_in_basin = set()
    traverse(point)

    return points_in_basin


def find_basins(low_points: List, array: List[List[int]]) -> List[set]:
    basins = []
    for low_point in low_points:
        basins.append(get_points_in_basin(low_point, array).union({low_point}))

    return basins


def main() -> None:
    with open("input", "r") as file:
        horizontal_lines = pad_array(parse_input(file))

    low_points = find_coordinates_of_low_points(horizontal_lines)
    basins = find_basins(low_points, horizontal_lines)

    three_largest_basis = sorted(basins, key=len, reverse=True)[:3]
    three_largest_basis = list(map(len, three_largest_basis))

    print(reduce(mul, three_largest_basis))


if __name__ == "__main__":
    main()
