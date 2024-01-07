import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with specific text labels
G.add_node("Python", label="Programming Language: Python")
G.add_node("NetworkX", label="Library: NetworkX")
G.add_node("Graph", label="Data Structure: Graph")

# Add edges with specific text labels
G.add_edge("Python", "NetworkX", label="Uses")
G.add_edge("NetworkX", "Graph", label="Builds")

# Draw the graph
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'label')

nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Save the graph as an image
plt.savefig("knowledge_graph.png", format="png")

# Show the graph
plt.show()
