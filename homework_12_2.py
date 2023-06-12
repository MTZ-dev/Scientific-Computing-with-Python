#EXERCISE 12.2

import networkx as nx
import matplotlib.pyplot as plt

number_of_nodes = 10

nodes = list(range(1, number_of_nodes + 1))

graph_1 = nx.Graph()

for node in nodes:
    graph_1.add_node(node)

for (a, b) in [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
                (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9),(9, 10), (2, 10)]:
    graph_1.add_edge(a, b)


nx.draw(graph_1, with_labels=True, font_weight='bold', node_size=1000, node_color='orange', edge_color='red', font_color='red')
plt.show()

