# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:50:34 2020

@author: Di Wang
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i=ListNode()
        j=i
        tem_ten=0
        while l1 or l2:
            tem=0
            if l1:
                tem+=l1.val
                l1=l1.next
            if l2:
                tem+=l2.val
                l2=l2.next
            tem_dig=(tem_ten+tem)%10
            tem_ten=(tem_ten+tem)//10
            j.next=ListNode(tem_dig)
            j=j.next
        if tem_ten:
            j.next=ListNode(1)
        j=i.next
        return i.next