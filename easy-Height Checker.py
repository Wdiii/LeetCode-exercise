# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def heightChecker(self, heights):
        #heights: List[int]) -> int:
        final=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=final[i]:
                count+=1
        return count
    
#see another solution from discussion
class Solution1:
    def heightChecker(self, heights):
        return len(heights) - sum([(x == y) for x,y in zip(heights, sorted(heights))])