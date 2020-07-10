# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def deckRevealedIncreasing(self, deck):
        #deck: List[int]) -> List[int]:
        deck.sort()
        res=[]
        while len(deck)>0:
            i=deck.pop()
            res.insert(0,i)
            res.insert(0,res.pop())
        res.append(res.pop(0))
        return res       
#逆向思维，一个排好序的list，取出最后的值，放到新的list的第一位，
#然后再把新list的最后一位拿到第一位，以此类推，这样就可以得到我们要的结果了。
