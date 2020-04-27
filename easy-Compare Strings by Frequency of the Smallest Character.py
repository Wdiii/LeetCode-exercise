# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        #queries: List[str], words: List[str]) -> List[int]:
        querie_lst, word_lst=[],[]
        for i in queries:
            querie_lst.append(i.count(min(i)))
        for j in words:
            word_lst.append(j.count(min(j)))
        result=[]
        for m in querie_lst:
            count=0
            for n in word_lst:
                if m<n:
                    count+=1
            result.append(count)
        return result
