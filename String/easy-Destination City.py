# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def destCity(self, paths):
        #paths: List[List[str]]) -> str:
        start=[]
        for i in range(len(paths)):
            start.append(paths[i][0])
        for j in range(len(paths)):
            if paths[j][1] not in start:
                return paths[j][1]
            
# another way
class Solution1:
    def destCity(self, paths):
        start = {i[0] for i in paths} 
        dest = {i[1] for i in paths} 
        return (dest - start).pop()