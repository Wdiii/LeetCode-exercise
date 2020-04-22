# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:25:58 2020

@author: Di Wang
"""

class Solution:
    def sortArrayByParityII(self, A):
        even=[]
        odd=[]
        output=[]
        for ele in A:
            if ele % 2 == 0:
                even.append(ele)
            else:
                odd.append(ele)
        for i in range(len(even)):
            output.append(even[i])
            output.append(odd[i])
        return output      


#another approach from LeetCode discussion:
class Solution1:
    def sortArrayByParityII(self, A):
        result = [0] * len(A)
        ptr_even , ptr_odd = 0, 1
        for ele in A:
            if ele % 2 == 0: 
                # Even Number
                result[ptr_even] = ele
                ptr_even += 2
            else:
                result[ptr_odd] = ele
                ptr_odd += 2
        return result