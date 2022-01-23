from statistics import median
from typing import Optional

from parse_input import parse_input

OPENING_CHARS = ["[", "{", "(", "<"]
CLOSING_CHARS = ["]", "}", ")", ">"]
OPPOSITES = {"[": "]", "{": "}", "(": ")", "<": ">"}
AUTOCOMPLETE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def get_incomplete_sequence(line: str) -> Optional[str]:
    opened_chars = []

    for char in line:
        if char in OPENING_CHARS:
            opened_chars.append(char)
        elif char in CLOSING_CHARS:
            if char == OPPOSITES[opened_chars[-1]]:
                opened_chars.pop()
            else:
                return False

    return "".join(reversed(opened_chars))


def get_autocomplete_score(sequence: str) -> int:
    score = 0

    for char in sequence:
        score = (5 * score) + AUTOCOMPLETE_SCORES[OPPOSITES[char]]

    return score


def main() -> None:
    with open("input", "r") as file:
        lines = parse_input(file)

    autocomplete_scores = []

    for line in lines:
        remaining_sequence = get_incomplete_sequence(line)
        if not remaining_sequence:
            continue
        autocomplete_scores.append(get_autocomplete_score(remaining_sequence))

    print(median(autocomplete_scores))


if __name__ == "__main__":
    main()
