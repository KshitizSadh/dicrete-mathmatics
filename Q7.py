class Graph:
    def __init__(self, num_vertices, adjacency_list):
        self.num_vertices = num_vertices
        self.adjacency_list = adjacency_list

    def is_complete_graph(self):
        for i in range(self.num_vertices):
            connected_vertices = set(self.adjacency_list[i])
            connected_vertices.discard(i)  # Remove self-loop if present
            if len(connected_vertices) != self.num_vertices - 1:
                return False
        return True

def main():
    # Example adjacency list representing a graph
    adjacency_list = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
    num_vertices = 4  # Number of vertices in the graph

    graph = Graph(num_vertices, adjacency_list)

    if graph.is_complete_graph():
        print("The given graph is a complete graph.")
    else:
        print("The given graph is not a complete graph.")

if __name__ == "__main__":
    main()