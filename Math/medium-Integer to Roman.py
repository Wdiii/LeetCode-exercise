# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:55:26 2020

@author: Di Wang
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        dic={'1000':'M','900':'CM','500':'D','400':'CD','100':'C','90':'XC','50':'L',
             '40':'XL','10':'X','9':'IX','5':'V','4':'IV','1':'I'}
        res=""
        for k,v in dic.items():
            count=num//int(k)
            if count!=0:
                res+=count*v
                num-=count*int(k)
        return res
        