# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def queensAttacktheKing(self, queens, king):
        #queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res=[]
        move=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
        for i in range(len(move)):
            x,y=king[0],king[1]
            while 0<=x<=7 and 0<=y<=7:
                x+=move[i][0]
                y+=move[i][1]
                if [x,y] in queens:
                    res.append([x,y])
                    break
        return res
