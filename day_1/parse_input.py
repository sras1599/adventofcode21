from io import TextIOWrapper

def parse_input(file: TextIOWrapper):
    return map(int, file.read().splitlines())