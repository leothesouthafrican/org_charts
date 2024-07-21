# visualization.py

import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

class FundStructureVisualizer:
    def __init__(self, fund_manager, node_size=3000, font_size=10, figure_size=(15, 10)):
        self.fund_manager = fund_manager
        self.G = nx.DiGraph()
        self.labels = {}
        self.shapes = {}
        self.node_size = node_size
        self.font_size = font_size
        self.figure_size = figure_size
        self._initialize_graph()

    def _initialize_graph(self):
        self._add_nodes(self.fund_manager)
        self._add_edges(self.fund_manager)

    def _add_edges(self, parent):
        for child in parent.children:
            self.G.add_edge(parent.name, child.name)
            self._add_edges(child)
        for related_entity in parent.relationships:
            self.G.add_edge(parent.name, related_entity.name)

    def _create_labels(self, entity):
        label = entity.name
        for key, value in entity.attributes.items():
            label += f"\n{key}: {value}"
        return label

    def _add_nodes(self, parent):
        self.labels[parent.name] = self._create_labels(parent)
        entity_type = type(parent).__name__

        shape_map = {
            'FundManager': 's',
            'MasterFund': 'D',
            'SubFund': 'o',
            'InvestmentVehicle': 'h',
            'Investor': '^'
        }

        self.shapes[parent.name] = shape_map.get(entity_type, 'o')  # default to circle if not found

        for child in parent.children:
            self.G.add_node(child.name)
            self.labels[child.name] = self._create_labels(child)
            self._add_nodes(child)

    def _draw_nodes(self, pos):
        node_shapes = set(self.shapes.values())
        for shape in node_shapes:
            nx.draw_networkx_nodes(
                self.G, pos, 
                nodelist=[s for s in self.shapes if self.shapes[s] == shape], 
                node_shape=shape, 
                node_size=self.node_size, 
                node_color="skyblue"
            )

    def _draw_labels(self, pos):
        for node, (x, y) in pos.items():
            plt.text(x, y, self.labels[node], 
                     fontsize=self.font_size, 
                     horizontalalignment='center', 
                     verticalalignment='center')

    def _create_legend(self):
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

    def visualize(self):
        pos = graphviz_layout(self.G, prog="dot")  # Use the 'dot' layout from Graphviz
        
        plt.figure(figsize=self.figure_size)  # Adjust the figure size to be user-defined or default
        
        self._draw_nodes(pos)
        nx.draw_networkx_edges(self.G, pos, arrows=True)
        self._draw_labels(pos)
        
        self._create_legend()
        plt.title("Fund Structure Chart")
        plt.show()
