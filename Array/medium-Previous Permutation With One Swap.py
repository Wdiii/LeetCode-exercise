# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:50:32 2020

@author: Di Wang
"""

class Solution:
    def prevPermOpt1(self, A):
        # A: List[int]) -> List[int]:
        if len(A)<=1:
            return A
        left,right=len(A)-2,len(A)-1
        while left>0 and A[left]<=A[left+1]:
            left-=1
        if left<0:
            return A
        while A[right]>=A[left]:
            right-=1
        while A[right]==A[right-1]:
            right-=1
        A[right],A[left]=A[left],A[right]
        return A
            