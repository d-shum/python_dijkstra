from dijkstra import dijkstra
from graph import graph

shortest_path = dijkstra(graph, start="A", finish="E")

print(shortest_path)  # (['A', 'C', 'D', 'E'], 9)
