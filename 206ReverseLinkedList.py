# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def rever(self,head: ListNode):
        if head.next==None:
            return head,head
        else:
            an,s=self.rever(head.next)
            an.next=head
            head.next=None
            return head,s
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        _,s=self.rever(head)
        return s

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        a=head
        b=head.next
        c=b.next
        a.next=None
        while c:
            b.next=a
            a=b
            b=c
            c=c.next
        b.next=a
        return b














