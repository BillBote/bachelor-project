"""
Date:17/03/2019
Author: Pengfei He
Aim: mhrw sampling
"""
from data import *
import numpy as np
import random
import networkx as nx

def mhrw(adj_raw,deg_raw,k):
    l=len(adj_raw)
    r0=random.sample(range(l),1)[0]
    edge=[]
    node=[]
    node.append(r0)
    i=0
    while i<k:
        node0=adj_raw[r0]
        index=list(np.array(range(1,l+1))*node0)
        while 0 in index:
            index.remove(0)
        if len(index)>0:
            r1=int(random.sample(index,1)[0])-1
        else:
            r0=random.sample(range(l),1)[0]
            node.append(r0)
            continue
        p=random.uniform(0,1)
        if deg_raw[r0]/deg_raw[r1]>=p:
            edge.append([r0,r1])
            node.append(r1)
            r0=r1
            i=i+1  
    return node,edge      

"""
# mhrw D-statistic

node,edge=mhrw(adj_facebook,deg_facebook,300)
node_mhrw,edge_mhrw=data_map(node,edge)
adj_mhrw=graph_adj(edge_mhrw,len(node_mhrw))
#graph_plot(edge)
deg_mhrw=graph_deg(adj_mhrw)
dist_mhrw=deg_dist(deg_mhrw)

x_list=[]
for key in dist_mhrw.keys():
    x_list.append(key)

ks_mhrw=KS_statistic(dist_facebook,dist_mhrw,x_list)
print(ks_mhrw)
"""