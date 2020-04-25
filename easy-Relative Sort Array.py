# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def relativeSortArray(self, arr1, arr2):
        #arr1: List[int], arr2: List[int]) -> List[int]
        remain=[]
        dic={}
        for i in arr1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            if i not in arr2:
                remain.append(i)
        lst=[]
        for j in arr2:
            lst.extend([j]*dic[j])
        return lst+sorted(remain)