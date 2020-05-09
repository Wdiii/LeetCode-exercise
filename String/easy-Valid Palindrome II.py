# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            l=0
            r=len(s)-1
            while l<=r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    a=s[l:r]
                    b=s[l+1:r+1]
                    return a==a[::-1] or b==b[::-1]