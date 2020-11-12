"""
Name:
PID:
"""

import random


def generate_edges(size, connectedness):
    """
    DO NOT EDIT THIS METHOD
    Generates undirected edges between vertices to form a graph
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """
    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                w = random.randint(1, 20)
                yield [i, j, w]


class Graph:
    """
    Class representing a Graph
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['start', 'destination', 'weight']

        def __init__(self, start, destination, weight):
            """
            DO NOT EDIT THIS METHOD
            :param start: represents the starting vertex of the edge
            :param destination: represents the destination vertex of the edge
            :param weight: represents the weight of the edge
            """
            self.start = start
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: edge to compare
            :return: Bool, True if same, otherwise False
            """
            return self.start == other.start and \
                   self.destination.vertex_id == other.destination.vertex_id \
                   and self.weight == other.weight

        def __repr__(self):
            return "Start: {self.start} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

        def get_start(self):
            """
            finds start vertex
            :return: start vertex
            """
            return self.start

        def get_destination(self):
            """
            finds the destination vertex
            :return: destinatoin vertex ie
            """
            return self.destination.vertex_id

        def get_weight(self):
            """
            finds weight of a vertex
            :return: weight of vertex
            """
            return self.weight

    class Vertex:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['vertex_id', 'edges', 'visited']

        def __init__(self, vertex_id):
            """
            DO NOT EDIT THIS METHOD
            :param vertex_id: represents the unique identifier of the vertex
            """
            self.vertex_id = vertex_id
            self.edges = {}
            self.visited = False

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: vertex to compare
            :return: Bool, True if the same, False otherwise
            """
            return self.vertex_id == other.vertex_id and \
                   self.edges == other.edges and self.visited == other.visited

        def __repr__(self):
            return f"Vertex: {self.vertex_id}"

        __str__ = __repr__

        def degree(self):
            """
            finds the degree of a vertex
            :return: degree
            """
            return len(self.edges)

        def visit(self):
            """
            changes visited value
            :return: true when visited
            """
            self.visited = True

        def insert_edge(self, destination, weight):
            """
            insert edge into edges
            :param destination: where the edge is finishing
            :param weight: weight of edge
            :return: returns where to put it in
            """
            self.edges[destination] = Graph.Edge(self.vertex_id, destination, weight)

        def get_edge(self, destination):
            """
            finds a edge
            :param destination: desitination of where to put edge
            :return: return
            """
            return self.edges[destination]

        def get_edges(self):
            """
            returns all the vertexes
            :return: list of all vertices
            """
            vertex_list = []
            for vertex in self.edges:
                vertex_list.append(vertex)
            return vertex_list

    def __init__(self):
        """
        DO NOT EDIT THIS METHOD
        """
        self.adj_map = {}
        self.size = 0

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.adj_map == other.adj_map and self.size == other.size

    def add_to_graph(self, source, dest=None, weight=0):
        """
        add a vertex into a graph
        :param source: source vertex
        :param dest: destination vertex
        :param weight: weight between two vertex
        :return: no return
        """
        if source is None and dest is None:
            return
        if source is None and dest is not None:
            self.adj_map[dest] = self.Vertex(dest)
            return

        if self.adj_map.get(source) is None:
            if self.adj_map.get(dest) is None:
                source_vertex = Graph.Vertex(source)
                self.size += 1
                if dest is not None:
                    dest_vertex = Graph.Vertex(dest)
                    source_edge = Graph.Edge(source_vertex.vertex_id, dest_vertex, weight)
                    dest_edge = Graph.Edge(dest_vertex.vertex_id, source_vertex, weight)
                    source_vertex.edges[dest_vertex.vertex_id] = source_edge
                    dest_vertex.edges[source_vertex.vertex_id] = dest_edge
                    self.adj_map[dest_vertex.vertex_id] = dest_vertex
                    self.size += 1
                self.adj_map[source_vertex.vertex_id] = source_vertex
            else:
                source_vertex = Graph.Vertex(source)
                dest_vertex = self.adj_map[dest]
                source_edge = Graph.Edge(source_vertex.vertex_id, dest_vertex, weight)
                source_vertex.edges[dest_vertex.vertex_id] = source_edge
                dest_edge = Graph.Edge(dest_vertex.vertex_id, source_vertex, weight)
                dest_vertex.edges[source_vertex.vertex_id] = dest_edge
                self.adj_map[source_vertex.vertex_id] = source_vertex
                self.size += 1
        else:
            if self.adj_map.get(dest) is None:
                if dest is not None:
                    source_vertex = self.adj_map[source]
                    dest_vertex = Graph.Vertex(dest)
                    source_edge = Graph.Edge(source_vertex.vertex_id, dest_vertex, weight)
                    dest_edge = Graph.Edge(dest_vertex.vertex_id, source_vertex, weight)
                    source_vertex.edges[dest_vertex.vertex_id] = source_edge
                    dest_vertex.edges[source_vertex.vertex_id] = dest_edge
                    self.adj_map[dest_vertex.vertex_id] = dest_vertex
                    self.size += 1
            else:
                source_vertex = self.adj_map[source]
                dest_vertex = self.adj_map[dest]
                source_edge = Graph.Edge(source_vertex.vertex_id, dest_vertex, weight)
                dest_edge = Graph.Edge(dest_vertex.vertex_id, source_vertex, weight)
                source_vertex.edges[dest_vertex.vertex_id] = source_edge
                dest_vertex.edges[source_vertex.vertex_id] = dest_edge

    def construct_graph_from_file(self, filename):
        """
        construct a graph from a file
        :param filename: file to construct from
        :return: no return
        """
        with open(filename) as fp:
            for line in fp:

                data = line.strip().split()
                if data[0] is not "":
                    if len(data) is 1:
                        source = data[0]
                        if source.isdigit():
                            self.add_to_graph(int(source))
                        else:
                            self.add_to_graph(source)
                    elif len(data) is 2:
                        source = data[0]
                        dest = data[1]
                        if source.isdigit():
                            source = int(source)
                        if dest.isdigit():
                            dest = int(dest)
                        self.add_to_graph(source, dest)
                    elif len(data) is 3:
                        source = data[0]
                        dest = data[1]
                        weight = data[2]
                        if source.isdigit():
                            source = int(source)
                        if dest.isdigit():
                            dest = int(dest)
                        self.add_to_graph(source, dest, int(weight))

    def get_vertex(self, vertex_id):
        """
        find the vertex
        :param vertex_id: vertex id to find
        :return: returns vertex if it is there
        """
        if self.adj_map.get(vertex_id) is not None:
            return self.adj_map[vertex_id]
        else:
            return None

    def get_vertices(self):
        """
        finds all vertices
        :return: list of all vertices
        """
        vertextList = []
        for vertex in self.adj_map:
            vertextList.append(vertex)
        return vertextList

    def bfs(self, start, target, path=None):
        """
        search through graph with BFS
        :param start: start vertex
        :param target: what we want to search till
        :param path: path used for recursion
        :return: list of vertices searched
        """
        possible_path = [[start]]
        if start == target:
            return [start]
        while len(possible_path) > 0:
            path = possible_path.pop(0)
            last_node = path[-1]
            if last_node == target:
                return path
            for adj_vertex in self.get_vertex(last_node).get_edges():
                adj_path = path.copy()
                adj_path.append(adj_vertex)
                possible_path.append(adj_path)
        return []

    def dfs(self, start, target, path=None):
        """
        DFS thought a graph
        :param start: start vertex
        :param target: end location
        :param path: path used for recurison
        :return: return the list of vertices used
        """
        self.get_vertex(start).visit()
        path.append(start)
        if start == target:
            return path
        else:
            for adj_vertex in self.get_vertex(start).get_edges():
                if self.get_vertex(adj_vertex).visited is False:
                    return_path = self.dfs(adj_vertex, target, path)
                    if return_path is not [] and return_path[-1] == target:
                        return return_path
        path.pop()
        return [start]


def quickest_route(filename, start, destination):
    """
    find the quests route between a start and end point
    :param filename: file to construct from
    :param start: start vertex
    :param destination: end vertex
    :return: shortest route
    """
    pass


if __name__ == "__main__":
    data1 = [784,
204,
127,
50,
33,
28,
19,
19,
6,
7,
6,
7,
4,
4,
5,
3,
3]
    count = 1
    list1 = []
    while count is not 18:
        for range1 in range(data1[count-1]):
            list1.append(count)
        count += 1
    print(list1)
