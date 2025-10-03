class Graph:
    def __init__(self):
        self.vertices = {}  # adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.vertices[from_vertex][to_vertex] = weight
        self.vertices[to_vertex][from_vertex] = weight  # undirected graph

    def dijkstra(self, start, end):
        distances = {v: float('inf') for v in self.vertices}
        previous = {v: None for v in self.vertices}
        distances[start] = 0

        unvisited = set(self.vertices.keys())

        while unvisited:
            current = min(unvisited, key=lambda vertex: distances[vertex])
            if distances[current] == float('inf') or current == end:
                break
            unvisited.remove(current)
            for neighbor, weight in self.vertices[current].items():
                alt = distances[current] + weight
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = current

        path, current = [], end
        while previous[current]:
            path.insert(0, current)
            current = previous[current]
        if path:
            path.insert(0, current)
        return path, distances[end] if distances[end] != float('inf') else ([], float('inf'))
