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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p=ListNode(None)
        p.next=head
        i=p
        while i.next:
            if i.next.val==val:
                i.next=i.next.next
            else:
                i=i.next
        return p.next
        