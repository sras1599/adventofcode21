from collections import Counter
from itertools import chain

from parse_input import parse_input


def main() -> None:
    with open("input", "r") as f:
        inputs, outputs = zip(*parse_input(f))

    counts_by_len = Counter(map(len, chain(*outputs)))

    print(sum((counts_by_len[count] for count in counts_by_len.keys() if count in [2, 3, 4, 7])))


if __name__ == "__main__":
    main()
