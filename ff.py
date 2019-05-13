"""
Date:14/04/2019
Author: Pengfei He
Aim: snow sampling method
"""
from data import *
import numpy as np
import random
import networkx as nx



def random_node(adj):
	return random.sample(range(len(adj)),1)[0]

def sample_node(nodes,k):
	if len(nodes)<=k:
		return nodes
	else:
		return random.sample(nodes,k)

def forestfire(adj,center,max_depth=1,current_depth=0,taboo_list=[],edge_list=[]):
	if current_depth==max_depth:
		print("out of depth")
		return edge_list
	if center in taboo_list:
		return edge_list
	else:
		taboo_list.append(center)

	friends=get_friend(adj,center)
	k=np.random.geometric(0.1)
	if len(friends)==0:
		friends_k=[random_node(adj)]
	else:
		friends_k=sample_node(friends,k)
	for node in friends_k:
		edge_list.append([center,node])
		edge_list=forestfire(adj,node,max_depth=max_depth,current_depth=current_depth+1,taboo_list=taboo_list,edge_list=edge_list)
	return edge_list

"""

# forest fire D-statistic

edge=forestfire(adj_facebook,random_node(adj_facebook),max_depth=20,current_depth=0)
node=[]
for i in range(len(edge)):
	node.append(edge[i][0])
	node.append(edge[i][1])
node_ff,edge_ff=data_map(node,edge)
adj_ff=graph_adj(edge_ff,len(node_ff))
deg_ff=graph_deg(adj_ff)
dist_ff=deg_dist(deg_ff)

x_list=[]
for key in dist_ff.keys():
    x_list.append(key)

ks_ff=KS_statistic(dist_facebook,dist_ff,x_list)
print(ks_ff)
"""
