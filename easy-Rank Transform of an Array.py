# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def arrayRankTransform(self, arr):
        #arr: List[int]) -> List[int]:
        lst=[]
        order=sorted(set(arr))
        for i in range(len(arr)):
            lst.append(order.index(arr[i])+1)
        return lst


#exceed time limit. Need to use dictionary.

class Solution1:
    def arrayRankTransform(self, arr):
        rank={}
        for i in sorted(set(arr)):
            rank[i]=len(rank)+1            
        return [rank[j] for j in arr]