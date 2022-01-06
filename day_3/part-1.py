from parse_input import parse_input

with open("input") as file:
    numbers = parse_input(file)

lists = list(zip(*map(list, numbers)))

from collections import Counter

most_common_bit = int("".join([i.most_common(1)[0][0] for i in map(Counter, lists)]), 2)
least_common_bit = int("".join([i.most_common()[-1][0] for i in map(Counter, lists)]), 2)

print(most_common_bit * least_common_bit)
