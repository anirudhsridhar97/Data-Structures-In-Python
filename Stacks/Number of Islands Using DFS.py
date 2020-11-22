# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:38:08 2020

@author: ANIRUDH
"""



"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


def numIslands(grid):
    
    #If Grid is Empty Return 0
    if not grid:
        return 0
    numberOfIsland=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            #Check if its a Land
            if grid[i][j]=='1':
                #Call Dfs to check whether Adjacent Neighbour is Land
                numberOfIsland+=dfs(grid,i,j)
                
    return numberOfIsland
def dfs(grid,i,j):
    
    
    if i<0 or i>=len(grid) or j<0  or j>=len(grid[i]) or grid[i][j]=='0':
        return 0
    
    #Mark In grid as visited
    grid[i][j]='0'
    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i,j-1)
    
    return 1
print(numIslands(grid))