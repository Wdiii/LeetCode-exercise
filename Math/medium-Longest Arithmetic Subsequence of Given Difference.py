# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def longestSubsequence(self, arr, difference):
        #arr: List[int], difference: int) -> int:
        dic={}
        for i in arr:
            dif=i-difference
            if dif in dic:
                dic[i]=dic[dif]+1
            else:
                dic[i]=1
        return max(dic.values())
