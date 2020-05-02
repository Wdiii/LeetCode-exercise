# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            n=len(needle)
            for i in range(len(haystack)-n+1):
                if haystack[i:i+n]==needle:
                    break
            return i