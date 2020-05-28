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
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        else:
            i=head
            j=head.next
            while j:
                tem=j.next
                j.next=i
                i=j
                j=tem
            head.next=None
            return i