# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numTimesAllBlue(self, light):
        #light: List[int]) -> int:
        res=0
        maxnum=0
        for i in range(len(light)):
            maxnum=max(maxnum,light[i]-1)
            if i==maxnum:
                res+=1
        return res
    