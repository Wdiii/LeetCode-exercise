# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        res=str(num)
        while len(res)!=1:
            tem=0
            for ele in res:
                tem+=int(ele)
            res=str(tem)
        return int(res)


# solution O(1) from Leetcode
class Solution1:
    def addDigits(self, num: int) -> int:
        if num<=9:
            return num
        if num%9==0:
            return 9
        else:
            return num%9
