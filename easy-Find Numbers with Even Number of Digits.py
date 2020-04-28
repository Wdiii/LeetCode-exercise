# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findNumbers(self, nums):
        #nums: List[int]) -> int:
        count=0
        for i in nums:
            if i > 9 and i < 100:
                count+=1
            elif i > 999 and i < 10000:
                count+=1
        return count

#solution from Leedcode
class Solution1:
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            j = str(i)
            if len(j) % 2 == 0 :
                count = count + 1          
        return count
