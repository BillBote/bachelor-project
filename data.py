"""
Date:17/03/2019
Author: Pengfei He
Aim: This module aims to load data and generate adjacency matrix，
draw graph plot, obtain degree distribution
Mostly for assistance functions
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def data_load(filename):  #data loading 
    data_raw=np.loadtxt(filename,dtype="int")
    l=len(data_raw)
    s=[]
    for i in range(l):
        s.append(data_raw[i][0])
        s.append(data_raw[i][1])
    s=list(set(s))
    dic={}
    for i in range(len(s)):
        dic[s[i]]=i
    for i in range(l):
        data_raw[i][0]=dic[data_raw[i][0]]
        data_raw[i][1]=dic[data_raw[i][1]]
    return data_raw


def graph_adj(data,node_num):  #adj matrix generator
    adj=np.zeros((node_num,node_num))
    for i in range(node_num):
        adj[data[i][0]][data[i][1]]=1
        adj[data[i][1]][data[i][0]]=1
    return adj

def graph_plot(data): # graph ploting
    G=nx.Graph()
    for i in range(len(data)):
        G.add_edge(data[i][0],data[i][1])
    nx.draw(G,node_size=3)
    plt.show()

def graph_deg(adj):  #generate degree matrix
    deg=[]
    for i in range(len(adj)):
        deg.append(np.sum(adj[i]))
    return deg

def deg_dist(data_deg):# generate distribution of degree
    deg_set=list(set(data_deg))
    dist={}
    for i in range(len(deg_set)):
        s=0
        for j in range(len(data_deg)):
            if data_deg[j]==deg_set[i]:
                s=s+1
        s=s/len(data_deg)
        dist[deg_set[i]]=s
    return dist

def ecdf(dist,x): #ecdf function for a certain distribution
    xs=[]
    for key in dist.keys():
        xs.append(key)
    xs=sorted(xs)
    p=0
    for i in range(len(xs)):
        if x>=xs[i]:
            p=p+dist[xs[i]]
    return(p)

def KS_statistic(dist1,dist2,x_list): # calculate ks statistic
    ks=0
    for x in x_list:
        if abs(ecdf(dist1,x)-ecdf(dist2,x))>ks:
            ks=abs(ecdf(dist1,x)-ecdf(dist2,x))
    return ks

def data_map(node,edge): #useful function 
    import copy
    node0=sorted(list(set(node)))
    node_new=list(range(len(node0)))
    edge_new=copy.deepcopy(edge)
    for i in range(len(edge)):
        edge_new[i][0]=node0.index(edge[i][0])
        edge_new[i][1]=node0.index(edge[i][1])
    return node_new,edge_new

def get_friend(adj,node):#obtain the friend node for a node
    friend=[]
    for i in range(len(adj)):
        if adj[node][i]==1:
            friend.append(i)
    return friend

def graph_plot(data): # graph ploting
    G=nx.Graph()
    for i in range(len(data)):
        G.add_edge(data[i][0],data[i][1])
    return G




data_facebook=data_load("facebook_combined.txt")
adj_facebook=graph_adj(data_facebook,4039)
deg_facebook=graph_deg(adj_facebook)
dist_facebook=deg_dist(deg_facebook)

