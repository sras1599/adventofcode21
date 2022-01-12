from collections import Counter
from typing import List

from parse_input import parse_input


class LanterfishCounter(Counter):
    def simulate_day(self):
        updated_counter = Counter()

        for state in self:
            state -= 1

            if state == -1:
                updated_counter.update({8: self[0], 6: self[0]})
            else:
                if state not in [6, 8]:
                    updated_counter[state] = self[state + 1]
                else:
                    updated_counter[state] = updated_counter[state] + self[state + 1]

        self.clear()
        self.update(updated_counter)

    def total(self):
        return sum(self.values())


if __name__ == "__main__":
    with open("input", "r") as file:
        fishes: List[int] = parse_input(file)

    reproduction_states = LanterfishCounter(fishes)
    for _ in range(256):
        reproduction_states.simulate_day()
    
    print(reproduction_states.total())