# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def diagonalSort(self, mat):
        #mat: List[List[int]]) -> List[List[int]]:
        col,row=len(mat[0]),len(mat)
        dic=collections.defaultdict(list)
        for i in range(row):
            for j in range(col):
                dic[i-j].append(mat[i][j])
        for d in dic:
            dic[d].sort()
        for r in range(row):
            for c in range(col):
                mat[r][c]=dic[r-c].pop(0)
        return mat
         
#defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值
#from collections import defaultdict
#dict1 = defaultdict(int) get 0
#dict2 = defaultdict(set) get set()
#dict3 = defaultdict(str) get 
#dict4 = defaultdict(list) get []
