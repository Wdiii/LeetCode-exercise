# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def advantageCount(self, A, B):
        #A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[0]*n
        a=sorted(A)
        b=sorted(list(range(n)),key=lambda x:B[x])
        #make list B in order
        l,r=0,n-1
        for i in range(n):
            if a[i]>B[b[l]]:
                res[b[l]]=a[i]
                l+=1
            else:
                res[b[r]]=a[i]
                r-=1
        return res
        