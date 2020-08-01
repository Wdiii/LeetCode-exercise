# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def tictactoe(self, moves):
        #moves: List[List[int]]) -> str:
        win=[[(0,0),(1,1),(2,2)],[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],
            [(1,0),(1,1),(1,2)],[(0,2),(1,2),(2,2)],[(2,0),(2,1),(2,2)],[(0,2),(1,1),(2,0)]]
        A,B=[],[]
        for a in moves[::2]:
            A.append((a[0],a[1]))
        for b in moves[1::2]:
            B.append((b[0],b[1]))
        A=sorted(A)
        B=sorted(B)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                for k in range(j+1,len(A)):
                    if [A[i],A[j],A[k]] in win:
                        return "A"
        for i in range(len(B)):
            for j in range(i+1,len(B)):
                for k in range(j+1,len(B)):
                    if [B[i],B[j],B[k]] in win:
                        return "B"
        if len(moves)==9:
            return "Draw"
        else:
            return "Pending"
          