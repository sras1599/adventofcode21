from io import TextIOWrapper
from typing import List


def parse_input(file: TextIOWrapper) -> List[str]:
    return [line.strip() for line in file]
