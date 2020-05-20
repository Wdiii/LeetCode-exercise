# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def largestTimeFromDigits(self, A):
        # A: List[int]) -> str:
        A.sort()
        for h in range(23,-1,-1):
            for m in range(59,-1,-1):
                time=[h//10, h%10, m//10, m%10]
                t=sorted(time)
                if t==A:
                    return str(time[0])+str(time[1])+":"+str(time[2])+str(time[3])
        return ""