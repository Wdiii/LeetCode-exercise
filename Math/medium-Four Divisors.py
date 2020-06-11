# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
class Solution:
    def sumFourDivisors(self, nums):
        #nums: List[int]) -> int:
        def FourFactors (N):
            lst=[]
            for i in range(1,int(math.sqrt(N))+1):
                if N%i==0:
                    lst.append(i)
                    if N//i!=i:
                        lst.append(N//i)
                if len(lst)>4:
                    break
            if len(lst)==4:
                return sum(lst)
            else:
                return 0
        res=0
        for ele in nums:
            res+=FourFactors(ele)
        return res
        