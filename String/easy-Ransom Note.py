# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res=True
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine=magazine.replace(ransomNote[i],"",1)
            else:
                res=False
        return res                