# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def rankTeams(self, votes):
        #votes: List[str]) -> str:
        dict={v: [0]*len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i,v in enumerate(vote):
                dict[v][i]-=1
        return "".join(sorted(votes[0], key=lambda x:dict[x]))
    