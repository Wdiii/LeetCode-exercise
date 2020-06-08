# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def validTicTacToe(self, board):
        #board: List[str]) -> bool:
        x_count,o_count = 0,0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    o_count += 1
                elif board[i][j] == 'X':
                    x_count += 1
        if o_count>x_count: 
            return False
        elif o_count<x_count-1: 
            return False
        elif o_count==x_count and self.win(board,"X"):
            return False
        elif o_count==x_count-1 and self.win(board,"O"):
            return False
        return True

#create a defination to test if X or O meet the requirement of wins   
    def win(self, board, P):
        # board is list[str]
        # P is 'X' or 'O' for two players
        for j in range(3):
            if all(board[i][j] == P for i in range(3)): return True
            if all(board[j][i] == P for i in range(3)): return True
        if board[0][0] == board[1][1] == board[2][2] == P: return True
        if board[0][2] == board[1][1] == board[2][0] == P: return True
        return False
    