# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def canJump(self, nums):
        #nums: List[int]) -> bool:
        maxjump=0
        for i in range(len(nums)):
            if i>maxjump:
                return False
            maxjump=max(maxjump,i+nums[i])
            if maxjump>=len(nums)-1:
                return True
    
#another solution about finding the 0 index
class Solution1:
    def canJump(self, nums):
        for i in range(len(nums)-1):
            if nums[i] != 0: continue#如果不为0，就进行下一次循环
            else:#找到了第i个数是0
                temp = nums[0:i+1][::-1]
                count = 0
                flag = False
                for item in temp:
                    if item > count: 
                        flag = True#可以跳到该位置
                        break
                    count += 1
                if flag == False: return False
        return True
