# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        start=1
        while len(str(N))!=len(str(start)):
            start*=2
        while len(str(N))==len(str(start)):
            if collections.Counter(str(N))==collections.Counter(str(start)):
                return True
            else:
                start*=2
        return False
#using collection.Counter to solve this problem
