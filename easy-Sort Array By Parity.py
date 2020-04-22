# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
'''

class Solution:
    def sortArrayByParity(self, A):
        even=[]
        odd=[]
        for ele in A:
            if ele % 2 == 0:
                even.append(ele)
            else:
                odd.append(ele)
        return even + odd
    