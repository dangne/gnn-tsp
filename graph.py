import pickle
import numpy as np
import networkx as nx


class Graph(object):
    def __init__(self, width, height, filepath="graph.pkl"):
        self.num_nodes = 0
        self.coordinates = []
        self.adj_matrix = np.empty((self.num_nodes, self.num_nodes))
        self.weight_matrix = np.empty((self.num_nodes, self.num_nodes))

        # Unnormalized forms (UNFs)
        self.unf_coordinates = []
        self.unf_weight_matrix = np.empty((self.num_nodes, self.num_nodes))

        self.width = width
        self.height = height

        with open(filepath, "rb") as f:
            self.coordinates = pickle.load(f)

        self.unf_coordinates = np.round(self.coordinates*[self.width, self.height]).astype(np.int32)
        self.num_nodes = len(self.coordinates)

        self.init_adj_matrix()
        self.init_weight_matrix()

    def init_adj_matrix(self):
        # Assume complete graph
        self.adj_matrix = np.ones((self.num_nodes, self.num_nodes))
        np.fill_diagonal(self.adj_matrix, 2)  # Special token for self-connections

    def init_weight_matrix(self):
        self.weight_matrix = np.empty((self.num_nodes, self.num_nodes))
        self.unf_weight_matrix = np.empty((self.num_nodes, self.num_nodes))

        for i in range(0, self.num_nodes):
            for j in range(i, self.num_nodes):
                x_i, y_i = self.coordinates[i]
                x_j, y_j = self.coordinates[j]
                unf_x_i, unf_y_i = self.unf_coordinates[i]
                unf_x_j, unf_y_j = self.unf_coordinates[j]
                self.weight_matrix[i][j] = np.sqrt((x_j - x_i) ** 2 + (y_j - y_i) ** 2)
                self.weight_matrix[j][i] = self.weight_matrix[i][j]
                self.unf_weight_matrix[i][j] = np.sqrt((unf_x_j - unf_x_i) ** 2 + (unf_y_j - unf_y_i) ** 2)
                self.unf_weight_matrix[j][i] = self.unf_weight_matrix[i][j]

    def get_subgraph(self, selected_node_ids):
        n = len(selected_node_ids)
        edges = np.ones((n, n))
        edges_values = np.empty((n, n))

        for i in range(0, n):
            for j in range(0, i):
                edges_values[i][j] = edges_values[j][i] = self.weight_matrix[selected_node_ids[i]][selected_node_ids[j]]

        nodes = np.ones(n)
        nodes_coord = self.coordinates[selected_node_ids]

        return edges, edges_values, nodes, nodes_coord
