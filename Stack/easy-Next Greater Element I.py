# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        #nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            a=-1
            p=nums2.index(i)
            for j in nums2[p:]:
                if j>i:
                    a=j
                    res.append(j)
                    break
            if a==-1:
                res.append(-1)
        return res


#solution from leetcode:    
class Solution1(object):
    def nextGreaterElement(self, findNums, nums):   
        st = []
        dic = {}        
        for num in nums:
            while len(st) and st[-1]<num:
                dic[st.pop()] = num
            st.append(num)
        return [dic.get(x,-1) for x in findNums]
        #if not in dic, use -1