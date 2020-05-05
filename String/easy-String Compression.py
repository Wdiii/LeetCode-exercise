# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def compress(self, chars):
        #chars: List[str]) -> int:
        n = len(chars)
        count = 1
        i = 0
        for j in range(1,n+1):
            if j < n and chars[j-1] == chars[j]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for m in str(count):
                        chars[i] = m
                        i += 1
                count = 1
        return i
            
#Input: ["a","a","b","b","c","c","c"]
#Output: ["a","2","b","2","c","3"]