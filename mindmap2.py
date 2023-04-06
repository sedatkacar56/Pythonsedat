import networkx as nx
import matplotlib.pyplot as plt
import pickle

# create an empty graph
G = nx.DiGraph()

# add the root node
root = 'AIM2_ASO'
G.add_node(root)

# create a mapping of node labels to node objects
nodes = {root: G.nodes[root]}

# loop to add nodes and edges based on user input
while True:
    # get user input for new node and parent node
    node_label = input("Enter a new node label (or 'q' to quit, 's' to save the figure, 'r' to remove the last node added): ")
    if node_label == 'q':
        break
    elif node_label == 's':
        plt.savefig('last_figure.png')
        print('Last figure saved')
        continue
    elif node_label == 'r':
        if len(G.nodes) > 1:
            last_node = list(G.nodes)[-1]
            G.remove_node(last_node)
            nodes.pop(last_node)
            print(f'Node {last_node} removed')
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True)
            plt.show()
        else:
            print('Cannot remove the root node')
        continue
    parent_label = input("Enter the parent node label: ")
    
    # add the new node to the graph and to the node mapping
    G.add_node(node_label)
    nodes[node_label] = G.nodes[node_label]
    
    # add an edge from the parent node to the new node
    G.add_edge(parent_label, node_label)
        # draw the updated graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

     # save the dictionary
    with open('graph_dict.pickle', 'wb') as f:
        pickle.dump(nodes, f)


# load the dictionary
with open('graph_dict.pickle', 'rb') as f:
    nodes = pickle.load(f)


# create the graph from the saved dictionary
G = nx.DiGraph()
for node_label in nodes:
    G.add_node(node_label)
for node_label in nodes:
    for neighbor_label in nodes[node_label]:
        G.add_edge(node_label, neighbor_label)

# draw the final graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()