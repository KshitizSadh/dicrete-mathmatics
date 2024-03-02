class Graph:
    def __init__(self, num_vertices, adjacency_matrix):
        self.num_vertices = num_vertices
        self.adjacency_matrix = adjacency_matrix

    def is_complete_graph(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i != j and self.adjacency_matrix[i][j] == 0:
                    return False
        return True

def main():
    # Example adjacency matrix representing a graph
    adjacency_matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]
    num_vertices = 4  # Number of vertices in the graph

    graph = Graph(num_vertices, adjacency_matrix)

    if graph.is_complete_graph():
        print("The given graph is a complete graph.")
    else:
        print("The given graph is not a complete graph.")

if __name__ == "__main__":
    main()