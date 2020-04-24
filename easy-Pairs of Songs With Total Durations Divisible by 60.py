# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numPairsDivisibleBy60(self, time):
        #time: List[int]) -> int:
        pair=0
        res= {}
        for i in time:
            if 60-i%60 in res:
                pair += res[60-i%60]    
            elif i%60 ==0 and 0 in res:
                pair += res[0]
                
            if i%60 not in res:
                res[i%60] = 0
            res[i%60] += 1
        return pair 
