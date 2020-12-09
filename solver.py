import os
import json
import argparse
import time

import numpy as np

import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.nn as nn

import matplotlib
import matplotlib.pyplot as plt

import networkx as nx
from sklearn.utils.class_weight import compute_class_weight

from tensorboardX import SummaryWriter
from fastprogress import master_bar, progress_bar

# Remove warning
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from scipy.sparse import SparseEfficiencyWarning
warnings.simplefilter('ignore', SparseEfficiencyWarning)

from config import *
from utils.graph_utils import *
from utils.google_tsp_reader import GoogleTSPReader
from utils.plot_utils import *
from models.gcn_model import ResidualGatedGCNModel
from utils.model_utils import *
from graph import Graph


if torch.cuda.is_available():
    print("CUDA available, using GPU")
    dtypeFloat = torch.cuda.FloatTensor
    dtypeLong = torch.cuda.LongTensor
    torch.cuda.manual_seed(1)
else:
    print("CUDA not available")
    dtypeFloat = torch.FloatTensor
    dtypeLong = torch.LongTensor
    torch.manual_seed(1)


class GNNSolver(object):
    def __init__(self, graph : Graph, config_path="configs/tsp20.json"):
        self.graph = graph
        self.config = get_config(config_path)
        print(f"Loaded {config_path}")

        self.init_gnn()

    def init_gnn(self):
        self.net = nn.DataParallel(ResidualGatedGCNModel(self.config, dtypeFloat, dtypeLong))
        if torch.cuda.is_available():
            self.net.cuda()

        # Load checkpoint
        log_dir = f"./logs/{self.config.expt_name}/"
        if torch.cuda.is_available():
            checkpoint = torch.load(log_dir+"best_val_checkpoint.tar")
        else:
            checkpoint = torch.load(log_dir+"best_val_checkpoint.tar", map_location='cpu')
        # Load network state
        self.net.load_state_dict(checkpoint['model_state_dict'])
        print(f"Loaded checkpoint from epoch {checkpoint['epoch']}")

        self.net.eval()

    def solve(self, selected_node_ids):
        edges, edges_values, nodes, nodes_coord = self.graph.get_subgraph(selected_node_ids)

        edges = np.expand_dims(edges, axis=0)
        edges_values = np.expand_dims(edges_values, axis=0)
        nodes = np.expand_dims(nodes, axis=0)
        nodes_coord = np.expand_dims(nodes_coord, axis=0)

        print(edges.shape)
        print(edges_values.shape)
        print(nodes.shape)
        print(nodes_coord.shape)

        batch_size = 1
        num_nodes = len(selected_node_ids)
        num_neighbors = -1  # self.config.num_neighbors
        beam_size = 1280  # self.config.beam_size
        test_filepath = self.config.test_filepath
        #dataset = iter(GoogleTSPReader(num_nodes, num_neighbors, batch_size, test_filepath))
        #batch = next(dataset)
        with torch.no_grad():
            # Convert batch to torch Variables
            x_edges = Variable(torch.LongTensor(edges).type(dtypeLong), requires_grad=False)
            x_edges_values = Variable(torch.FloatTensor(edges_values).type(dtypeFloat), requires_grad=False)
            x_nodes = Variable(torch.LongTensor(nodes).type(dtypeLong), requires_grad=False)
            x_nodes_coord = Variable(torch.FloatTensor(nodes_coord).type(dtypeFloat), requires_grad=False)

            # Compute class weights
            #edge_labels = y_edges.cpu().numpy().flatten()
            #edge_cw = compute_class_weight("balanced", classes=np.unique(edge_labels), y=edge_labels)
            #print("Class weights: {}".format(edge_cw))

            # Forward pass
            y_preds = self.net.forward(x_edges, x_edges_values, x_nodes, x_nodes_coord)  # , y_edges, edge_cw)

            # Get batch beamsearch tour prediction
            bs_nodes = beamsearch_tour_nodes_shortest(
                y_preds, x_edges_values, beam_size, batch_size, num_nodes, dtypeFloat, dtypeLong, probs_type='logits')

            # Compute mean tour length
            pred_tour_len = mean_tour_len_nodes(x_edges_values, bs_nodes)
            #gt_tour_len = np.mean(batch.tour_len)
            print("Predicted tour length: {:.3f} (mean)".format(pred_tour_len))  # \nGroundtruth tour length: {:.3f} (mean)".format(pred_tour_len, gt_tour_len))

            # Sanity check
            for idx, nodes in enumerate(bs_nodes):
                if not is_valid_tour(nodes, num_nodes):
                    print(idx, " Invalid tour: ", nodes)

            route = []
            for idx in bs_nodes[0]:
                route.append(selected_node_ids[idx])
            route.append(route[0])

            return route
