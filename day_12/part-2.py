from typing import Dict, List, Set

from parse_input import parse_input


class CaveSystem:
    def __init__(self, points: List[List[str]]) -> None:
        self.points = points
        self.graph = self._build_graph()
        self.eligible_paths = set()

    def _build_graph(self) -> Dict[str, Set[str]]:
        _graph: Dict[str, Set[str]] = {}

        for start, end in self.points:
            _graph.setdefault(start, set()).add(end)
            _graph.setdefault(end, set()).add(start)

        return _graph

    def traverse_paths(self):
        small_caves = [cave for cave in self.graph if cave.islower() and not cave in ["start", "end"]]

        for cave in small_caves:
            self.small_cave_with_most_connections = cave
            for node in self.graph["start"]:
                current_path = f"start->{node}"
                self.traverse_path(node, current_path)

    def traverse_path(self, current_node: str, current_path: str):
        for node in self.graph[current_node]:
            if node.islower() and node in current_path:
                if not node == self.small_cave_with_most_connections:
                    continue
                if current_path.count(node) >= 2:
                    continue
                self.traverse_path(node, f"{current_path}->{node}")
                continue

            if node == "end":
                self.eligible_paths.add(f"{current_path}->end")
                continue
            self.traverse_path(node, f"{current_path}->{node}")

    @property
    def num_paths(self):
        return len(self.eligible_paths)


def main() -> None:
    with open("input", "r") as file:
        points = parse_input(file)

    cave_system = CaveSystem(points)
    cave_system.traverse_paths()

    print(cave_system.num_paths)


if __name__ == "__main__":
    main()
