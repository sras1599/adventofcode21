from io import TextIOWrapper

def parse_input(file: TextIOWrapper) -> list:
    """
    Parse input file and return list of lines
    """
    return [int(number) for number in file.readline().split(",")]