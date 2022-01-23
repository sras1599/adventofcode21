from __future__ import annotations

from typing import List, Optional

from parse_input import parse_input


class DumboOctopus:
    def __init__(self, x: int, y: int, energy_level: int) -> None:
        self.x = x
        self.y = y
        self.energy_level = energy_level
        self.has_flashed = False
        self.coordinate_to_octopus = {}

    def flash(self, adjacent_octopuses: Optional[List[DumboOctopus]]):
        self.on_flash()

        for octopus in adjacent_octopuses:
            if not octopus.has_flashed:
                octopus.simulate_step()

        for octopus in adjacent_octopuses:
            if octopus.can_flash:
                octopus.flash(octopus.get_adjacent_octopuses())

    def simulate_step(self):
        self.energy_level += 1

    def on_flash(self):
        self.energy_level = 0
        self.has_flashed = True
        DumboOctopuses.NUM_FLASHES += 1

    def get_adjacent_octopuses(self) -> List[DumboOctopus]:
        x, y = self.x, self.y

        candidate_coordinates = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x - 1, y - 1),
            (x + 1, y + 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
        ]

        candidate_coordinates = [
            coordinate
            for coordinate in candidate_coordinates
            if coordinate[0] not in [-1, 10] and coordinate[1] not in [-1, 10]
        ]

        return [self.coordinate_to_octopus[coordinate] for coordinate in candidate_coordinates]

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.energy_level})"

    @property
    def can_flash(self) -> bool:
        return self.energy_level > 9


class DumboOctopuses:
    NUM_FLASHES = 0

    def __init__(self, octopuses: List[DumboOctopus]) -> None:
        self.octopuses = octopuses
        coordinate_to_octopus = {(octopus.x, octopus.y): octopus for octopus in self.octopuses}

        for octopus in self.octopuses:
            octopus.coordinate_to_octopus = coordinate_to_octopus

    def simulate_step(self):
        for octopus in self.octopuses:
            octopus.simulate_step()

        for octopus in self.octopuses:
            if octopus.can_flash:
                octopus.flash(octopus.get_adjacent_octopuses())

        for octopus in self.octopuses:
            octopus.has_flashed = False


def get_octopuses(energy_levels: List[List[int]]) -> Optional(List[DumboOctopus]):
    octopuses: List[DumboOctopus] = []

    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            octopuses.append(DumboOctopus(i, j, energy_levels[i][j]))

    return octopuses


def main() -> None:
    with open("input", "r") as file:
        energy_levels = parse_input(file)

    dumbo_octopuses = DumboOctopuses(get_octopuses(energy_levels))

    for _ in range(100):
        dumbo_octopuses.simulate_step()

    print(DumboOctopuses.NUM_FLASHES)


if __name__ == "__main__":
    main()
