"""
Date:17/03/2019
Author: Pengfei He
Aim: get random node sample and obtain its ecdf and KS-statistic
"""
from data import *
import numpy as np
import random
import networkx as nx


node=random.sample(range(4039),1000)
node=sorted(node)
adj_node=[]
for i in node:
	adj=list(adj_facebook[i][node])
	adj_node.append(adj)
deg_node=graph_deg(adj_node)
dist_node=deg_dist(deg_node)

x_list=[]
for key in dist_node.keys():
	x_list.append(key)
ks_node=KS_statistic(dist_facebook,dist_node,x_list)
print(ks_node)

