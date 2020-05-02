# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        #strs: List[str]) -> str:
        if strs==[] or "" in strs:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            result=""
            min_strs=min(len(ele) for ele in strs)
            for j in range(min_strs):
                flag=1
                for i in range(1,len(strs)):
                    if strs[0][j]!=strs[i][j]:
                        flag=0
                        break
                if flag:
                    result+=strs[0][j]
                else:
                    break
            return result
