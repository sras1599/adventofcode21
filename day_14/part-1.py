from collections import Counter
from itertools import tee
from typing import Dict

from parse_input import parse_input


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    yield from zip(a, b)


class Polymer:
    def __init__(self, template: str, instructions: Dict[str, str]) -> None:
        self.instructions = instructions
        self.pair_counter = Counter(pairwise(template))
        self.char_counter = Counter(template)

    def insert_pairs(self, steps: int):
        for _ in range(steps):
            self.pair_counter = self.insert_pair()

    def insert_pair(self):
        new_counter = Counter()

        for pair, count in self.pair_counter.items():
            result = self.instructions.get(pair[0] + pair[1])

            self.char_counter[result] += count
            new_counter[tuple(pair[0] + result)] += count
            new_counter[tuple(result + pair[1])] += count

        return new_counter

    @property
    def score(self):
        return self.char_counter.most_common()[0][1] - self.char_counter.most_common()[-1][1]


def main():
    with open("input", "r") as file:
        template, instructions = parse_input(file)

    polymer = Polymer(template, instructions)

    polymer.insert_pairs(steps=10)
    print(polymer.score)


if __name__ == "__main__":
    main()
