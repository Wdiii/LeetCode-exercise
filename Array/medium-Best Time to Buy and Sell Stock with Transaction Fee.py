# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxProfit(self, prices, fee):
        #prices: List[int], fee: int) -> int:
        if len(prices)==0:
            return 0
        a=0
        b=-prices[0]
        for i in range(1,len(prices)):
            c=a
            a=max(a,b+prices[i]-fee)
            b=max(b,c-prices[i])
        return max(a,b)
        