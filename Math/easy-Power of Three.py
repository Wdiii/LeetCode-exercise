# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>=3:
            n=n/3
        return n==1.0
    
# solution from leetcode
class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
       return n > 0 and 1162261467 % n ==0