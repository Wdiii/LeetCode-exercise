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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        first=head
        while l1!=None and l2!=None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else :
                head.next = l1
                l1 = l1.next
            head=head.next
        if l1!=None:
            head.next = l1
        elif l2!=None:
            head.next = l2
        return first.next
