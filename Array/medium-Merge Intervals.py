# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def merge(self, intervals):
        #intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort()
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]<intervals[i+1][0]:
                i+=1
            else:
                intervals[i]=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                intervals.pop(i+1)
        return intervals
