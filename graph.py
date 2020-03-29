from typing import Dict, List


class Node:
    def __init__(self, name: str, distance: float):
        self.name = name
        self.distance = distance

    def __repr__(self) -> str:
        return self.name + ":" + str(self.distance)


Graph = Dict[str, List[Node]]
graph = {
    "A": [Node("C", 3), Node("B", 7)],
    "C": [Node("B", 1), Node("D", 2), Node("A", 3)],
    "B": [Node("C", 1), Node("D", 2), Node("E", 6), Node("A", 7)],
    "D": [Node("C", 2), Node("B", 2), Node("E", 4)],
    "E": [Node("D", 4), Node("B", 6)]
}