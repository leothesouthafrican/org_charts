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

def add_nodes(G, parent, labels, shapes):
    labels[parent.name] = create_labels(parent)
    entity_type = type(parent).__name__
    
    if entity_type == 'FundManager':
        shapes[parent.name] = 's'  # square
    elif entity_type == 'MasterFund':
        shapes[parent.name] = 'D'  # diamond
    elif entity_type == 'SubFund':
        shapes[parent.name] = 'o'  # circle
    elif entity_type == 'InvestmentVehicle':
        shapes[parent.name] = 'h'  # hexagon
    elif entity_type == 'Investor':
        shapes[parent.name] = '^'  # triangle
    
    for child in parent.children:
        G.add_node(child.name)
        labels[child.name] = create_labels(child)
        add_nodes(G, child, labels, shapes)

def visualize_structure(fund_manager):
    G = nx.DiGraph()
    labels = {}
    shapes = {}
    add_nodes(G, fund_manager, labels, shapes)
    add_edges(G, fund_manager)
    pos = nx.spring_layout(G)
    
    # Draw nodes with shapes
    node_shapes = set(shapes.values())
    for shape in node_shapes:
        nx.draw_networkx_nodes(G, pos, nodelist=[s for s in shapes if shapes[s] == shape], node_shape=shape, node_size=3000, node_color="skyblue")
    
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_weight="bold")
    
    # Create a legend
    legend_labels = {
        's': 'Fund Manager',
        'D': 'Master Fund',
        'o': 'Sub Fund',
        'h': 'Investment Vehicle',
        '^': 'Investor'
    }
    for shape, label in legend_labels.items():
        plt.scatter([], [], c="skyblue", marker=shape, label=label)
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper left')

    plt.title("Fund Structure Chart")
    plt.show()
