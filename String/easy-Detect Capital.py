# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<=1:
            return True
        else:
            L=word.lower()
            U=word.upper()
            R=U[0]+L[1:]
            if word==L or word==U or word==R:
                return True
            else:
                return False

#can also use 
#return True if(word.isupper()) or (word.islower()) or (word[0].isupper() and word[1:].islower()) else False