from io import TextIOWrapper

def parse_input(file: TextIOWrapper) -> list:
    return file.read().splitlines()