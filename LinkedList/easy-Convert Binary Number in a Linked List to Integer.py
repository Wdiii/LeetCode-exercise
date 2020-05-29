# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:21:14 2020

@author: Di Wang
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        i=head
        s=""
        while i:
            s+=str(i.val)
            i=i.next
        return int(s,2)