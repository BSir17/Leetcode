# -*- coding:utf-8 -*-
# Code by Fan.Bai

def judeleft(i,j,grid):
    if j==0:
        return 1
    if grid[i][j-1]==0:
        return 1
    return 0

def juderight(i,j,grid):
    if j==len(grid[0])-1:
        return 1
    if grid[i][j+1]==0:
        return 1
    return 0

def judeup(i,j,grid):
    if i==0:
        return 1
    if grid[i-1][j]==0:
        return 1
    return 0

def judedown(i,j,grid):
    if i==len(grid)-1:
        return 1
    if grid[i+1][j]==0:
        return 1
    return 0

class Solution:
    def islandPerimeter(self, grid) -> int:
        sum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                sum+=judedown(i,j,grid)
                sum+=judeleft(i,j,grid)
                sum+=judeup(i,j,grid)
                sum+=juderight(i,j,grid)
        return (sum)

ss=[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(Solution().islandPerimeter(ss))













