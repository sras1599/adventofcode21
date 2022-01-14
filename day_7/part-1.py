# TODO: optimize
from collections import Counter

from parse_input import parse_input

if __name__ == "__main__":
    with open("input", "r") as file:
        horizontal_positions = parse_input(file)

    direction_to = dict.fromkeys(horizontal_positions, 0)
    counts = Counter(horizontal_positions)

    for key in direction_to.keys():
        for dup in direction_to.keys():
            if dup == key:
                continue
            diff = abs(dup - key)
            total_diff = diff * counts[dup]
            direction_to[key] += total_diff
    
    print(min(direction_to.values()))
