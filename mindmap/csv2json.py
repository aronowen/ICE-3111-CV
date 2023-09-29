#!/usr/bin/env python3

import sys, copy
import pandas as pd
import networkx as nx
from networkx.readwrite import json_graph
from community import community_louvain

# import matplotlib.cm as cm
# import matplotlib.pyplot as plt

NoneType = type(None)


def numberOfLinks(input_df, node_name):
    nb_links = 0
    test = input_df["Source"] == node_name
    nb_links += input_df["Source"][test].count()

    test = input_df["Target"] == node_name
    nb_links += input_df["Target"][test].count()

    return nb_links

def main():

    global id_of_first_author_column
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: ", sys.argv[0], " input.csv")
    else:
        input_df = pd.read_csv(sys.argv[1])

        # Get the nodes
        nodes = copy.deepcopy(input_df["Source"].unique().tolist())
        for node in input_df["Target"].unique():
            if not node in nodes:
                nodes.append(node)

        # Capitalize all the strings
        nodes = [item for item in nodes]

        # Get the links
        edges = []
        for source, target in zip(input_df["Source"], input_df["Target"]):
            source = source
            target = target

            idx1 = nodes.index(source)
            idx2 = nodes.index(target)
            edges.append([idx1, idx2])

        G = nx.Graph() # Initialize a Graph object
        G.add_nodes_from(range(len(nodes))) # Add nodes to the Graph
        G.add_edges_from(edges) # Add edges to the Graph
        partition = community_louvain.best_partition(G)

        # draw the graph
        pos = nx.spring_layout(G)
        # color the nodes according to their partition
        # cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
        # nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
        #                        cmap=cmap, node_color=list(partition.values()))
        # nx.draw_networkx_edges(G, pos, alpha=0.5)
        # plt.show()

        groups = []
        for k, v in partition.items():
            # partition[k] = v + 1
            groups.append((partition[k]))

        print('{\n\t"directed": false,\n\t"multigraph": false,\n\t"graph": {},\n\t"nodes": [')

        for i, value in enumerate(zip(nodes, groups)):

            node_name = value[0]
            group  = value[1]

            if i < len(nodes) - 1:
                print('\t\t{"id":' + str(i) + ', "name": \"' + node_name.title() + "\", \"weight\": " + str(numberOfLinks(input_df, node_name)) + ", \"group\": " + str(group) + '},')
            else:
                print('\t\t{"id":' + str(i) + ', "name": \"' + node_name.title() + "\", \"weight\": " + str(numberOfLinks(input_df, node_name)) + ", \"group\": " + str(group) + '}')

        print("\t],\n\t\"links\": [")

        for i, key in enumerate(edges):
            if i < len(edges) - 1:
                print('\t\t{"source": ', key[0], ', "target": ', key[1], ', "weight": ', str(1.0), '},')
            else:
                print('\t\t{"source": ', key[0], ', "target": ', key[1], ', "weight": ', str(1.0), '}')

        print("\t]\n}")

if __name__ == '__main__':
    main()
