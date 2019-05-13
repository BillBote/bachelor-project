from data import *
import numpy as np
import random
import networkx as nx




def rwrw(adj_raw,k):
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
			edge.append([r0,r1])
			node.append(r1)
			r0=r1
			i=i+1
		else:
			r0=random.sample(range(l),1)[0]
			node.append(r0)
	return node,edge

def rwrw_dist(data_deg):# generate distribution of degree
    while 0 in data_deg:
        data_deg.remove(0)
    deg_set=list(set(data_deg))
    s_total=0
    for i in range(len(data_deg)):
    	s_total=s_total+1/data_deg[i]
    dist={}
    for i in range(len(deg_set)):
        s=0
        for j in range(len(data_deg)):
            if data_deg[j]==deg_set[i]:
                s=s+1/deg_set[i]
        s=s/s_total
        dist[deg_set[i]]=s
    return dist

"""
# rwrw D-statistic

node,edge=rwrw(adj_facebook,100)
node_rwrw,edge_rwrw=data_map(node,edge)
adj_rwrw=graph_adj(edge_rwrw,len(node_rwrw))
#graph_plot(edge)
deg_rwrw=graph_deg(adj_rwrw)
dist_rwrw=rwrw_dist(deg_rwrw)

x_list=[]
for key in dist_rwrw.keys():
	x_list.append(key)
ks_rwrw=KS_statistic(dist_facebook,dist_rwrw,x_list)

print(ks_rwrw)
"""