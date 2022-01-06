from parse_input import parse_input

with open("input") as file:
    instructions = parse_input(file)

depth = aim = horizontal_position = 0

for instruction, value in instructions:
    if instruction == "down":
        aim += value
    elif instruction == "up":
        aim -= value
    else:
        horizontal_position += value
        depth += aim * value

print(horizontal_position * depth)
