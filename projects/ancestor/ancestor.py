from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for a in ancestors:
        graph.add_vertex(a[0])
        graph.add_vertex(a[1])
        graph.add_edge(a[1], a[0])
    res = graph.dft(starting_node)
    if res != starting_node:
        return res
    else:
        return -1


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8))
