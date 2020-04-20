# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:38:46 2020

@author: Di Wang
"""

class Solution:
    def numMagicSquaresInside(self, grid):
        if len(grid)<3 or len(grid[0])<3:
            return 0
        else:
            count=0
            for i in range(len(grid)-2):
                for j in range(len(grid[0])-2):
                    a,b,c = grid[i][j], grid[i][j+1], grid[i][j+2]
                    d,e,f = grid[i+1][j],grid[i+1][j+1], grid[i+1][j+2]
                    g,k,l = grid[i+2][j],grid[i+2][j+1], grid[i+2][j+2]
                    
                    unique_values = len({a,b,c,d,e,f,g,k,l})==9
                    value_1_9 = all(x in [1,2,3,4,5,6,7,8,9] for x in [a,b,c,d,e,f,g,k,l])
                    
                    if unique_values and value_1_9:
                        if a+b+c==d+e+f==g+k+l==a+d+g==b+e+k==c+f+l==a+e+l==c+e+g:
                            count+=1
        return count

#solution from Leetcode                

class Solution2(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in xrange(R-2):
            for c in xrange(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans