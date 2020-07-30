# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        #candies: List[int], extraCandies: int) -> List[bool]:
        greatest=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=greatest:
                res.append(True)
            else:
                res.append(False)
        return res
            
# a faster solytion from leetcode
class Solution2:
    def kidsWithCandies(self, candies, extraCandies):
        maxx = max(candies)
        return [True if maxx <= kid + extraCandies else False for kid in candies]
    