# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return True
        else:
            lst=[]
            i=head
            while i:
                lst.append(i.val)
                i=i.next
            return lst==lst[::-1]
    