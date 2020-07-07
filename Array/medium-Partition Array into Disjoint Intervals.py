# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:01:30 2020

@author: Di Wang
"""

class Solution:
    def partitionDisjoint(self, A):
        #A: List[int]) -> int:
        for i in range(len(A)-1):
            if max(A[:i+1])<=min(A[i+1:]):
                return i+1
#time limit exceeded 
#在Python中虽然max()和min()函数很好用，但是它们本质上也是一次遍历，只不过对使用者透明，使用的话会超出时间限制。

class Solution2:
    def partitionDisjoint(self, A):
        left=1
        tem=maxtem=A[0]
        for i in range(left,len(A)):
            if A[i]<tem:
                left=i+1
                tem=maxtem
            if A[i]>maxtem:
                maxtem=A[i]        
        return left
