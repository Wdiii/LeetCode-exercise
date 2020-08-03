# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def kWeakestRows(self, mat, k):
        # mat: List[List[int]], k: int) -> List[int]:
        dict={}
        for m,n in enumerate(mat):
            dict[m]=sum(n)
        lst=sorted(dict.items(),key=lambda x:(x[1],x[0]))
        res=[]
        for i in range(k):
            res.append(lst[i][0])
        return res
    