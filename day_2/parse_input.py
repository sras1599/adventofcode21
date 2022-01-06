from io import TextIOWrapper


def parse_input(file: TextIOWrapper) -> list:
    instructions = []

    for line in file:
        keyword, value = line.split()
        instructions.append((keyword, int(value)))

    return instructions
