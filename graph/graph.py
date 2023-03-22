class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for node in self.adj_list:
            print(node, ':', self.adj_list[node])

    def add_node(self, node):
        if node not in self.adj_list.keys():
            self.adj_list[node] = []
            return True
        return False
    
    def add_edge(self, n1, n2):
        if n1 in self.adj_list.keys() and n2 in self.adj_list.keys():
            self.adj_list[n1].append(n2)
            self.adj_list[n2].append(n1)
            return True
        return False
    
    def remove_edge(self, n1, n2):
        if n1 in self.adj_list.keys() and n2 in self.adj_list.keys():
            try:
                self.adj_list[n1].remove(n2)
                self.adj_list[n2].remove(n1)
            except ValueError:
                pass
            return True
        return False

    def remove_node(self, node):
        if node in self.adj_list.keys():
            for other_node in self.adj_list[node]:
                self.adj_list[other_node].remove(node)
            del self.adj_list[node]
            return True
        return False

if __name__ == '__main__':
    my_graph = Graph()
    my_graph.add_node('A')
    my_graph.add_node('B')
    my_graph.add_node('C')
    my_graph.add_edge('A', 'B')
    my_graph.add_edge('A', 'C')
    my_graph.add_edge('B', 'C')
    my_graph.print_graph()
    
    # my_graph.remove_edge('A', 'B')
    # my_graph.print_graph()

    # my_graph.add_node('D')
    # my_graph.remove_edge('A', 'D')

    print("Graph 2")
    g2 = Graph()
    g2.add_node('A')
    g2.add_node('B')
    g2.add_node('C')
    g2.add_node('D')
    g2.add_edge('A','B')
    g2.add_edge('A','C')
    g2.add_edge('A','D')
    g2.add_edge('B','D')
    g2.add_edge('C','D')
    g2.print_graph()

    print("Remove D")
    g2.remove_node('D')
    g2.print_graph()