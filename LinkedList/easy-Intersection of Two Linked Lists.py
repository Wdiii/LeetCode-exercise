# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i,j = headA,headB
        while(i!=j):
            i=headB if i==None else i.next
            j=headA if j==None else j.next
        return i