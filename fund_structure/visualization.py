import networkx as nx
import matplotlib.pyplot as plt

def add_edges(G, parent):
    for child in parent.children:
        G.add_edge(parent.name, child.name)
        add_edges(G, child)

def create_labels(entity):
    label = entity.name
    for key, value in entity.attributes.items():
        label += f"\n{key}: {value}"
    return label

def add_nodes(G, parent, labels):
    labels[parent.name] = create_labels(parent)
    for child in parent.children:
        G.add_node(child.name)
        labels[child.name] = create_labels(child)
        add_nodes(G, child, labels)

def visualize_structure(fund_manager):
    G = nx.DiGraph()
    labels = {}
    add_nodes(G, fund_manager, labels)
    add_edges(G, fund_manager)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color="skyblue", font_size=8, font_weight="bold", verticalalignment='center')
    plt.title("Fund Structure Chart")
    plt.show()
