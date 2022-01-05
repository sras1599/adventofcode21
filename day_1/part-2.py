from parse_input import parse_input

with open("input") as file:
    numbers = list(parse_input(file))

lists = numbers, numbers[1:], numbers[2:]

pairs = list(zip(*lists))


def is_increasing(curr, next):
    return sum(next) > sum(curr)


print(sum([is_increasing(pairs[i], pairs[i + 1]) for i in range(len(pairs) - 1)]))
