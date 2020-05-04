# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowes={'a','e','i','o','u','A','E','I','O','U'}
        vow=[]
        lst=list(s)
        for i in lst:
            if i in vowes:
                vow.append(i)
        for j in range(len(lst)):
            if lst[j] in vowes:
                lst[j]=vow.pop()
        return "".join(lst)