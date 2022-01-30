from io import TextIOWrapper


def parse_input(file: TextIOWrapper):
    points = []
    instructions = []

    for line in file:
        line = line.strip()

        if line.isspace() or line == "":
            continue
        if line.startswith("fold"):
            instruction = line.split(" ")[-1].split("=")
            instructions.append((instruction[0], int(instruction[1])))
        else:
            points.append(tuple(map(int, line.split(","))))

    return points, instructions
