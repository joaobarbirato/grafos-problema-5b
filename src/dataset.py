import networkx as nx

# Creating nodes
G = nx.Graph()
for i in range(0,20):
    G.add_node(str(i))

# Creating edges
edgeFile = open('./data/edges.txt', 'rt')
edges = edgeFile.readlines()
for i in range(0,20):
    G.add_edge((edges[i].split(' '))[0], (edges[i].split(' '))[1])

edgeFile.close()
# end dataset