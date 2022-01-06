from parse_input import parse_input

with open("input") as file:
    instructions = parse_input(file)

values = dict.fromkeys(list(zip(*instructions))[0], 0)

for keyword, value in instructions:
    values[keyword] += value

print(values["forward"] * (values["down"] - values["up"]))
