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

def snowBall(adj,center,max_depth=1,current_depth=0,taboo_list=[],edge_list=[],k=1):
	if current_depth==max_depth:
		print("out of depth")
		return edge_list
	if center in taboo_list:
		return edge_list
	else:
		taboo_list.append(center)

	friends=get_friend(adj,center)
	if len(friends)==0:
		friends_k=[random_node(adj)]
	else:
		friends_k=sample_node(friends,k)
	for node in friends_k:
		edge_list.append([center,node])
		edge_list=snowBall(adj,node,max_depth=max_depth,current_depth=current_depth+1,taboo_list=taboo_list,edge_list=edge_list,k=k)
	return edge_list

"""
# snowball D-statistic

edge=snowBall(adj_facebook,random_node(adj_facebook),max_depth=20,current_depth=0,k=20)
node=[]
for i in range(len(edge)):
	node.append(edge[i][0])
	node.append(edge[i][1])
node_sbs,edge_sbs=data_map(node,edge)
adj_sbs=graph_adj(edge_sbs,len(node_sbs))
deg_sbs=graph_deg(adj_sbs)
dist_sbs=deg_dist(deg_sbs)

x_list=[]
for key in dist_sbs.keys():
    x_list.append(key)

ks_sbs=KS_statistic(dist_facebook,dist_sbs,x_list)
print(ks_sbs)
"""
