from io import TextIOWrapper


def parse_input(file: TextIOWrapper):
    template = file.readline().strip()
    insertion_rules = {}

    for line in file:
        if line.strip() == "":
            continue
        else:
            rule = line.strip().split(" -> ")
            insertion_rules[rule[0]] = rule[1]

    return template, insertion_rules
