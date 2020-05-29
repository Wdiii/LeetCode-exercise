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
    def middleNode(self, head: ListNode) -> ListNode:
        i=head
        l=0
        while i:
            l+=1
            i=i.next
        i=head
        c=0
        while c < l//2:
            c+=1
            i=i.next
        return i
        