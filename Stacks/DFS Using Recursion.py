# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:06:04 2020

@author: ANIRUDH
"""
"""
Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is 
O(V + E), where V is the number of vertices and E is the number of edges. In case of DFS on a tree, 
the time complexity is O(V), where V is the number of nodes.

"""

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            
        
dfs(visited,graph,'A')