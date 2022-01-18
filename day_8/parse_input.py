from io import TextIOWrapper
from typing import List


def parse_input(file: TextIOWrapper) -> List[list]:
    inputs = []
    outputs = []

    for line in file:
        input, *output = line.strip().split("|")
        inputs.append(input.split())
        outputs.append(output[0].split())

    return list(zip(inputs, outputs))