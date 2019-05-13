from data import *
from rw import *
from mhrw import *
from rwrw import *
from ff import *
from sbs import *
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt


# rw graph
g_rw=[]
for i in [100,200,400,600,1000,1200,1500,2000,2200]:
    nodes,edges=rw(adj_facebook,i)
    G=nx.Graph()
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    g_rw.append(G)

#rwrw graph
g_rwrw=[]
for i in [100,200,400,600,1000,1200,1500,2000,2200]:
    nodes,edges=rwrw(adj_facebook,i)
    G=nx.Graph()
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    g_rwrw.append(G)


#forestfire graph
g_ff=[]
for i in range(9):
    center=random_node(adj_facebook)
    edges=forestfire(adj_facebook,center)
    G=nx.Graph()
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    g_ff.append(G)

# mhrw graph
g_mhrw=[]
for i in [100,200,400,600,1000,1200,1500,2000,2200]:
    nodes,edges=mhrw(adj_facebook,deg_facebook,i)
    G=nx.Graph()
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    g_mhrw.append(G)


# sbs graph
g_sbs=[]

for i in range(9):
    center=random_node(adj_facebook)
    edges=snowBall(adj_facebook,center,k=20)
    G=nx.Graph()
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    g_sbs.append(G)


# rw statistic
node_rw=[]
edge_rw=[]
dia_rw=[]
clu_rw=[]
cc_rw=[]
for i in range(len(g_rw)):
    node_rw.append(g_rw[i].number_of_nodes())
    edge_rw.append(g_rw[i].number_of_edges())
    dia_rw.append(nx.diameter(g_rw[i]))
    clu_rw.append(nx.average_clustering(g_rw[i]))
    cc_rw.append(nx.number_connected_components(g_rw[i]))

# rwrw statistic

node_rwrw=[]
edge_rwrw=[]
dia_rwrw=[]
clu_rwrw=[]
cc_rwrw=[]
for i in range(len(g_rwrw)):
    node_rwrw.append(g_rwrw[i].number_of_edges())
    edge_rwrw.append(g_rwrw[i].number_of_nodes())
    dia_rwrw.append(nx.diameter(g_rwrw[i]))
    clu_rwrw.append(nx.average_clustering(g_rwrw[i]))
    cc_rwrw.append(nx.number_connected_components(g_rwrw[i]))


# mhrw statistic

node_mhrw=[]
edge_mhrw=[]
dia_mhrw=[]
clu_mhrw=[]
cc_mhrw=[]
for i in range(len(g_mhrw)):
    node_mhrw.append(g_mhrw[i].number_of_nodes())
    edge_mhrw.append(g_mhrw[i].number_of_edges())
    dia_mhrw.append(nx.diameter(g_mhrw[i]))
    clu_mhrw.append(nx.average_clustering(g_mhrw[i]))
    cc_mhrw.append(nx.number_connected_components(g_mhrw[i]))


# ff statistic

node_ff=[]
edge_ff=[]
dia_ff=[]
clu_ff=[]
cc_ff=[]
for i in range(len(g_ff)):
    node_ff.append(g_ff[i].number_of_nodes())
    edge_ff.append(g_ff[i].number_of_edges())
    dia_ff.append(nx.diameter(g_ff[i]))
    clu_ff.append(nx.average_clustering(g_ff[i]))
    cc_ff.append(nx,number_connected_components(g_ff[i]))

# sbs statistic

node_sbs=[]
edge_sbs=[]
dia_sbs=[]
clu_sbs=[]
cc_sbs=[]
for i in range(len(g_sbs)):
    node_sbs.append(g_sbs[i].number_of_nodes())
    edge_sbs.append(g_sbs[i].number_of_edges())
    dia_sbs.append(nx.diameter(g_sbs[i]))
    clu_sbs.append(nx.average_clustering(g_sbs[i]))
    cc_sbs.append(nx.number_connected_components(g_sbs[i]))



