# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        result=["1"]
        for i in range(n):
            count=0
            number=result[i]
            char=number[0]
            output=""
            for j in range(len(number)):
                if number[j]==char:
                    count+=1
                else:
                    output+=str(count)
                    output+=str(char)
                    char=number[j]
                    count=1
            output+=str(count)
            output+=str(char)
            result.append(output)
        return result[n-1]