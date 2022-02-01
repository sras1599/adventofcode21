from __future__ import annotations

import heapq
from typing import Dict, List, Optional, Tuple, TypeVar

T = TypeVar("T")


class PriorityQueue:
    def __init__(self) -> None:
        self.elements: List[Tuple[float, T]] = []

    def put(self, item: T, priority: float) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

    @property
    def empty(self):
        return not self.elements


class Point:
    def __init__(self, x: int, y: int, cost: int) -> None:
        self.x = x
        self.y = y
        self.cost = cost

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __lt__(self, other: Point) -> bool:
        return self.cost < other.cost
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Grid:
    def __init__(self, elements: List[List[int]]) -> None:
        self.elements: List[List[Point]] = []

        for y, row in enumerate(elements):
            self.elements.append([])
            for x, element in enumerate(row):
                self.elements[y].append(Point(x, y, element))

    def heuristic(self, point_a: Point, point_b: Point) -> float:
        return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)

    def cost(self, from_point: Point, to_point: Point):
        return to_point.cost

    def neighbors(self, point: Point) -> List[Point]:
        neighbors = []

        if not point.x == self.width - 1:
            neighbors.append(self.elements[point.y][point.x + 1])
        if not point.y == self.height - 1:
            neighbors.append(self.elements[point.y + 1][point.x])
        if not point.x == 0:
            neighbors.append(self.elements[point.y][point.x - 1])
        if not point.y == 0:
            neighbors.append(self.elements[point.y - 1][point.x])

        return neighbors

    @property
    def start(self) -> Point:
        return self.elements[0][0]

    @property
    def end(self) -> Point:
        return self.elements[-1][-1]

    @property
    def height(self):
        return len(self.elements)

    @property
    def width(self):
        return len(self.elements[0])


def a_star_search(grid: Grid):
    frontier = PriorityQueue()
    frontier.put(grid.start, 0)
    came_from: Dict[Point, Optional[Point]] = {}
    cost_so_far: Dict[Point, float] = {}
    came_from[grid.start] = None
    cost_so_far[grid.start] = 0

    while not frontier.empty:
        current: Point = frontier.get()

        if current == grid.end:
            break

        for next in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:

                cost_so_far[next] = new_cost
                priority = new_cost + grid.heuristic(grid.end, next)
                frontier.put(next, priority)
                came_from[next] = current

    return cost_so_far[grid.end]
