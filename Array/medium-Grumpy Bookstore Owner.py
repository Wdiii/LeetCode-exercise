# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        #customers: List[int], grumpy: List[int], X: int) -> int:
        n=len(customers)
        res=0
        for i in range(n):
            if grumpy[i]==0:
                res+=customers[i]
        diff=[]
        for j in range(n):
            diff.append(customers[j]*grumpy[j])
        tem=0
        for x in range(n-X+1):
            tem=max(tem,sum(diff[x:x+X]))
        return res+tem
        