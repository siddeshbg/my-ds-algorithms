class Graph:
    def __init__(self, num_of_nodes) -> None:
        self.num_of_nodes = num_of_nodes + 1
        self.matrix = [[0 for i in range(num_of_nodes + 1)] for j in range(num_of_nodes + 1)]

    def within_bounds(self, n1, n2):
        return (n1 >= 0 and n1 <= self.num_of_nodes and
                n2 >=0 and n2 <= self.num_of_nodes)
    
    def add_edge(self, n1, n2):
        if self.within_bounds(n1, n2):
            self.matrix[n1][n2] = 1
    
    def print_graph(self):
        for i in range(self.num_of_nodes):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    print (i, "->", j)

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(4,5)
    g.print_graph()
