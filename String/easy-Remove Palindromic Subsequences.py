# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif s==s[::-1]:
            return 1
        else:
            return 2