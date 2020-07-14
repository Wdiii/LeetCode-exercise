# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def countCharacters(self, words, chars):
        #words: List[str], chars: str) -> int:
        dic_chars=collections.Counter(chars)
        res=0
        for word in words:
            dic_word=collections.Counter(word)
            if all(dic_word[w]<=dic_chars[w] for w in word):
                res+=len(word)
        return res
                