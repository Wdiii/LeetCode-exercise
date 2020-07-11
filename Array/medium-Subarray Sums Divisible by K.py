# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def subarraysDivByK(self, A, K):
        #A: List[int], K: int) -> int:
        rem,count=0,0
        dic={0:1}
        for i in A:
            rem=(rem+i)%K
            if rem in dic:
                count+=dic[rem]
            dic[rem]=dic.get(rem,0)+1
        return count
    