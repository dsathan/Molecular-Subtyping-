# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:04:53 2021

@author: user1
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
df = pd.read_csv('Pam_Msdec1.csv')
    
B = nx.Graph()
B.add_nodes_from(df['Pam'], bipartite=0)
B.add_nodes_from(df['Cluster'], bipartite=1)
B.add_weighted_edges_from(
    [(row['Pam'], row['Cluster'], 1) for idx, row in df.iterrows()], 
    weight='weight')


pos = {node:[0, i] for i,node in enumerate(df['Pam'])}
pos.update({node:[1, i] for i,node in enumerate(df['Cluster'])})
nx.draw(B, pos, with_labels=False)
for p in pos:  # raise text positions
    pos[p][1] += 0.25
nx.draw_networkx_labels(B, pos)
plt.show()

my_matching = bipartite.matching.minimum_weight_full_matching(B, df['Pam'], "weight")
print(my_matching)