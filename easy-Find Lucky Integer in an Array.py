# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findLucky(self, arr):
        #arr: List[int]) -> int:
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        lucky=[]
        for j in dic:
            if dic[j]==j:
                lucky.append(j)
        if lucky==[]:
            return -1
        else:
            return max(lucky)