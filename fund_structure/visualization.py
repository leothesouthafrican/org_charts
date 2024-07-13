import networkx as nx
import matplotlib.pyplot as plt

def add_edges(G, parent):
    for child in parent.children:
        G.add_edge(parent.name, child.name)
        add_edges(G, child)

def visualize_structure(fund_manager):
    G = nx.DiGraph()
    add_edges(G, fund_manager)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
    plt.title("Fund Structure Chart")
    plt.show()
