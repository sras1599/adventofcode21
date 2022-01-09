from io import TextIOWrapper


def parse_input(file: TextIOWrapper):
    grids = [[]]
    numbers = (int(i) for i in file.readline().rstrip().split(","))

    for line in filter(None, map(str.rstrip, file)):
        if len(grids[-1]) == 5:
            grids.append([])

        grids[-1].append([int(i) for i in line.split()])

    return numbers, grids
