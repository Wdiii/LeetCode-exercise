# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_num=list(filter(str.isalnum, s.lower())) #get character and number
        for i in range(len(char_num)//2):
            if char_num[i]!=char_num[len(char_num)-1-i]:
                break
                return False
            else:
                return True   