# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        lst=[]
        s=S.split()
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        for i in range(len(s)):
            if s[i][0] in vowel or len(s[i])==1:
                lst.append(s[i]+"ma"+"a"*(i+1))
            else:
                lst.append(s[i][1:]+s[i][0]+"ma"+"a"*(i+1))
        return " ".join(lst)