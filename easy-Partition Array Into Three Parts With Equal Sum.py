# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def canThreePartsEqualSum(self, A):
        #A: List[int]) -> bool:
        if sum(A) %3 !=0:
            return False
        target=int(sum(A)/3)
        part=-target
        count=0
        for i in A:
            if count==2:
                return True
            else:
                part+=i
                if part==0:
                    count+=1
                    part=-target
        return False