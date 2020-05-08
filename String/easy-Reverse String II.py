# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s[::-1]
        elif len(s)<=k*2:
            return s[0:k][::-1] + s[k:]
        else:
            return s[0:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:],k)


#other result from leetcode
class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join([s[i: i + k][::-1] + s[i + k: i + 2 * k] for i in range(0, len(s), 2 * k)])
