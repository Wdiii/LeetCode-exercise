# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def canReorderDoubled(self, A):
        #A: List[int]) -> bool:
        A.sort()
        dic=collections.Counter(A)
        for i in range(len(A)):
            if A[i]==0 or A[i] not in dic: 
                continue
            elif A[i]<0:
                if A[i]%2==1 or dic[A[i]/2]==0:
                    return False
                else:
                    dic[A[i]/2]-=dic[A[i]]
                    if dic[A[i]/2]==0:
                        del dic[A[i]/2]
                    del dic[A[i]]
            else:
                if dic[A[i]*2]==0:
                    return False
                else:
                    dic[A[i]*2]-=dic[A[i]]
                    if dic[A[i]*2]==0:
                        del dic[A[i]*2]
                    del dic[A[i]]
        return True
    