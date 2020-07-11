# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def shipWithinDays(self, weights, D):
        #weights: List[int], D: int) -> int:
        right=sum(weights)
        left=max(right//D,max(weights))
        while left<=right:
            tem,day,current=(right+left)//2,1,0
            for w in weights:
                if w+current>tem:
                    day+=1
                    current=0
                current+=w
            if day>D:
                left=tem+1
            else:
                right=tem-1
        return left
        