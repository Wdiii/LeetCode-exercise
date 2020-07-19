# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def canMakePaliQueries(self, s, queries):
        #s: str, queries: List[List[int]]) -> List[bool]:
        res=[]
        for left,right,k in queries:
            if k>=13 or self.identify(s[left:right+1],k):
                res.append(True)
            else:
                res.append(False)
        return res
    def identify(self,word,k):
        dic=collections.Counter(word)
        odd=0
        for key,value in dic.items():
            if value%2:
                odd+=1
        return odd//2 <=k
#exceed time limited

class Solution1:
    def canMakePaliQueries(self, s, queries):
        alphabet = set(s) #无需处理26个字母，只需处理在s中出现过的字母
        dic = dict()
        for char in alphabet:
            dic[char] = [0 for _ in range(len(s))]
        for i, ch in enumerate(s): #计算出现次数的前缀和
            for char in alphabet:
                if ch == char:
                    if i > 0:
                        dic[ch][i] = dic[ch][i - 1] + 1
                    else:
                        dic[ch][i] = 1
                else:
                    if i > 0:
                        dic[char][i] = dic[char][i - 1]             
        res = []
        for left, right, k in queries:
            odd_cnt = 0
            for char in alphabet:
                if left > 0:
                    if (dic[char][right] - dic[char][left - 1]) % 2 == 1:# 直接相减得到字母出现次数
                        odd_cnt += 1
                else:
                    if dic[char][right] % 2 == 1:
                        odd_cnt += 1
            if odd_cnt // 2 <= k:
                res.append(True)
            else:
                res.append(False)                
        return res
