from typing import Optional

from parse_input import parse_input

OPENING_CHARS = ["[", "{", "(", "<"]
CLOSING_CHARS = ["]", "}", ")", ">"]
OPPOSITES = {"[": "]", "{": "}", "(": ")", "<": ">"}
ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_first_illegal_char(line: str) -> Optional[str]:
    opened_chars = []

    for char in line:
        if char in OPENING_CHARS:
            opened_chars.append(char)
        elif char in CLOSING_CHARS:
            if char == OPPOSITES[opened_chars[-1]]:
                opened_chars.pop()
            else:
                return char


def main() -> None:
    with open("input", "r") as file:
        lines = parse_input(file)

    error_score = 0

    for line in lines:
        first_illegal_char = find_first_illegal_char(line)
        error_score += ERROR_SCORES.get(first_illegal_char, 0)

    print(error_score)


if __name__ == "__main__":
    main()
