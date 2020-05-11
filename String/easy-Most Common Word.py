# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class WrongSolution:
    def mostCommonWord(self, paragraph, banned):
        #paragraph: str, banned: List[str]) -> str:
        lst=[s.strip("!?',;.") for s in paragraph.lower().split()]
        dic={}
        for i in lst:
            if i not in banned:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        return max(dic, key=dic.get)

#show error in "a, a, a, a, b,b,b,c, c", ["a"]

#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列
#max(dic, key=dic.get) --> get the maximum value in key


import re
# https://www.runoob.com/python/python-reg-expressions.html

class Solution:
    def mostCommonWord(self, paragraph, banned):
        p = re.compile(r"[!?',;.]")
        lst=p.sub(' ',paragraph.lower()).split()
        dic={}
        for i in lst:
            if i not in banned:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        return max(dic, key=dic.get)
