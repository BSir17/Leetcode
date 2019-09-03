# -*- coding:utf-8 -*-
# Code by Fan.Bai


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#倒数第n个，则fast指针指向第n，low指向第1，则fast指向最后.low指向第n
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s=ListNode(-1)
        s.next=head
        fast=low=s
        for i in range(n):
            fast=fast.next
        while fast.next:
            fast=fast.next
            low=low.next
        low.next=low.next.next
        return s.next














