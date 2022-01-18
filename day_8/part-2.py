from typing import Dict, List

from parse_input import parse_input


class SafeDict(dict):
    def __missing__(self, key):
        return ""


class SevenSegmentDisplay:
    UNIQUE_LENGTHS = [1, 3, 4, 7]

    def __init__(self, inputs: List[str], outputs: List[str]):
        self.inputs_by_len: Dict[int, List[str]] = {}

        for input in inputs:
            self.inputs_by_len.setdefault(len(input), []).append(set(input))

        self.outputs = [set(output) for output in outputs]

        self.positions = self.decode_positions()

    def decode_positions(self) -> Dict[str, str]:
        positions = {}

        positions["top_center"] = "".join(set.difference(self.inputs_by_len[3][0], self.inputs_by_len[2][0]))

        for input in self.inputs_by_len[6]:
            if set.difference(self.inputs_by_len[4][0], input) == set():
                positions["bottom_left"] = "".join(
                    set.difference(self.inputs_by_len[7][0], set.union(self.inputs_by_len[4][0], input))
                )
            if len(set.intersection(input, self.inputs_by_len[2][0])) == 1:
                positions["top_right"] = "".join(set.difference(self.inputs_by_len[7][0], input))

        positions["bottom_right"] = "".join(set.difference(self.inputs_by_len[2][0], set(positions["top_right"])))
        positions["bottom_center"] = "".join(
            set.difference(
                self.inputs_by_len[7][0],
                set.union(self.inputs_by_len[4][0], {positions["bottom_left"], positions["top_center"]}),
            )
        )

        for input in self.inputs_by_len[6]:
            if len(set.difference(self.inputs_by_len[7][0], set.union(input, set(positions.values())))) == 1:
                positions["center"] = "".join(set.difference(self.inputs_by_len[7][0], input))

        positions["top_left"] = "".join(set.difference(self.inputs_by_len[7][0], set(positions.values())))

        return positions

    @property
    def output(self):
        digit = ""

        for output in self.outputs:
            for number, required_segments in self.number_mapping.items():
                if set(required_segments.format_map(SafeDict(self.positions))) == output:
                    digit += str(number)
                    break

        return int(digit)

    @property
    def number_mapping(self) -> Dict[int, str]:
        return {
            0: "{top_center}{top_right}{bottom_right}{bottom_center}{bottom_left}{top_left}",
            1: "{top_right}{bottom_right}",
            2: "{top_center}{top_right}{bottom_center}{bottom_left}{center}",
            3: "{top_center}{top_right}{bottom_right}{bottom_center}{center}",
            4: "{top_right}{bottom_right}{top_left}{center}",
            5: "{top_center}{top_left}{bottom_center}{bottom_right}{center}",
            6: "{top_center}{top_left}{bottom_left}{bottom_right}{center}{bottom_center}",
            7: "{top_center}{top_right}{bottom_right}",
            8: "{top_center}{top_right}{top_left}{bottom_left}{bottom_center}{bottom_right}{center}",
            9: "{top_center}{top_right}{top_left}{bottom_right}{bottom_center}{center}",
        }


def main() -> None:
    with open("input", "r") as f:
        inputs, outputs = zip(*parse_input(f))

    cum_sum = 0

    for i, o in zip(inputs, outputs):
        display = SevenSegmentDisplay(i, o)
        cum_sum += display.output

    print(cum_sum)


if __name__ == "__main__":
    main()
