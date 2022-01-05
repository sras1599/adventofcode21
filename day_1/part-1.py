from itertools import tee
from typing import Generator, Tuple

from parse_input import parse_input

with open("input") as file:
    numbers: map = parse_input(file)


def pairwise(iterable: Generator) -> zip:
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def is_pair_ascending(pair: Tuple) -> bool:
    return pair[0] < pair[1]


is_increasing = filter(bool, map(is_pair_ascending, pairwise(numbers)))

print(sum(is_increasing))
