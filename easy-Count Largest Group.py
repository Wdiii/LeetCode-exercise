# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countLargestGroup(self, n):
        #n: int) -> int:
        #use dictionary
        count = {} 
        for i in range(1, n+1):
            tmp = 0
            while i:
                tmp += i % 10
                i //= 10
            if tmp in count:
                count[tmp] += 1
            else:
                count[tmp] = 1        
        count=list(count.values())
        return count.count(max(count))