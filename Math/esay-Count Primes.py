# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        nums = [None] * n
        nums[0],  nums[1] = False, False
        for i in range(n):
            if nums[i] == None:
                nums[i] = True
                for j in range(i+i, n, i):
                    nums[j] = False
        return sum(nums)
