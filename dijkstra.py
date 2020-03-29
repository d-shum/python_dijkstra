from math import inf
from graph import Node, Graph


def dijkstra(graph: Graph, start: str, finish: str):
    # dict where key is node name and value previous node and cumulative distance from start to node name
    shortest_distance = {
        start: Node(start, 0)
    }

    # priority queue or heap
    heap = [Node(start, 0)]

    visited = set()

    while len(heap) > 0:
        current_element = heap.pop(0)
        current_element_name = current_element.name

        visited.add(current_element_name)

        neighbours = graph[current_element_name]

        for neighbour in neighbours:
            neighbour_name = neighbour.name
            # current shortest distance to neighbour from start
            try:
                current_shortest_distance = shortest_distance[neighbour_name].distance
            except KeyError:
                # if there is no previous value set it to inf
                current_shortest_distance = inf

            # distance from start to current element plus distance from current to neighbour
            current_distance = shortest_distance[current_element_name].distance + neighbour.distance
            # if current distance from start to neighbour less than in dict update it
            if current_distance < current_shortest_distance:
                shortest_distance[neighbour_name] = Node(current_element_name,
                                                         current_distance)

            if neighbour.name not in visited:
                heap.append(neighbour)

        # sort to preserve order of priority queue
        heap.sort(key=lambda node: node.distance)

    # building the path back to start
    path = [finish]
    path_length = shortest_distance[finish].distance

    while True:
        head = path[0]
        if head == start:
            break
        previous = shortest_distance[head].name
        path.insert(0, previous)

    return path, path_length
