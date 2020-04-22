# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:25:58 2020

@author: Di Wang
"""

class Solution:
    def hasGroupsSizeX(self, deck):
        if len(deck)==1:
            return False
        lst=list(set(deck))
        count_lst=[]
        for i in lst:
            count_lst.append(deck.count(i))
        n=min(count_lst)
        for j in range(2,n+1):
            all_count = True
            for ele in count_lst:
                if ele%j != 0:
                    all_count=False
                    break
            if all_count==True:
                return True
        return False           
