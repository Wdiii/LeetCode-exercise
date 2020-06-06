# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def solveEquation(self, equation: str) -> str:
        left,right=equation.split("=")
        if left[0]=="-":
            left="0"+left
        if right[0]=="-":
            right="0"+right
        left = left.replace('-', '+-')
        right = right.replace('-', '+-')
        left_x,left_v,right_x,right_v=0,0,0,0
        for i in left.split("+"):
            if "x" in i:
                if i=="x":
                    left_x+=1
                elif i=="-x":
                    left_x-=1
                else:
                    left_x+=int(i[:-1])
            else:
                left_v+=int(i)
        for j in right.split("+"):
            if "x" in j:
                if j=="x":
                    right_x+=1
                elif j=="-x":
                    right_x-=1
                else:
                    right_x+=int(j[:-1])
            else:
                right_v+=int(j)
        left_x-=right_x
        right_v-=left_v
        if left_x!=0 and right_v==0:
            return "x=0"
        elif left_x==0 and right_v==0:
            return "Infinite solutions"
        elif left_x==0 and right_v!=0:
            return "No solution"
        else:
            return "x="+str(right_v//left_x)
                