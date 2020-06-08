# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def escapeGhosts(self, ghosts, target):
        #ghosts: List[List[int]], target: List[int]) -> bool:
        route=abs(target[0])+abs(target[1])
        catch=abs(ghosts[0][0]-target[0])+abs(ghosts[0][1]-target[1])
        if len(ghosts)==1:
            return route<catch
        else:
            for i in range(1,len(ghosts)):
                catch=min(catch,abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1]))
            return route<catch

#shorter solution
class Solution1:
    def escapeGhosts(self, ghosts, target):
        required_moves = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if (abs(ghost[0]-target[0]) + abs(ghost[1]-target[1]) <= required_moves):
                return False           
        return True