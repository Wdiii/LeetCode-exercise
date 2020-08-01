# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def isPossibleDivide(self, nums, k):
        # nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        dic=collections.Counter(nums)
        listdic=sorted(dic)
        for key in listdic:
            val=dic[key]
            if val:
                for i in range(key,key+k):
                    if dic[i]<val:
                        return False
                    dic[i]-=val
        return True
        