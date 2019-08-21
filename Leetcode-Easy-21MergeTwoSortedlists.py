# -*- coding:utf-8 -*-
# Code by Fan.Bai


#按顺序合并就行了
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 or l2)==False:
            return None
        if not l1:return l2
        if not l2:return l1
        if l1.val<l2.val:
            s=l1
            l1=l1.next
        else:
            s=l2
            l2=l2.next
        loc=s
        while l1 and l2:
            if l1.val<l2.val:
                loc.next=l1
                l1=l1.next
            else:
                loc.next=l2
                l2=l2.next
            loc=loc.next
        if l1:
            loc.next=l1
        if l2:
            loc.next=l2
        return s


a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(4)
a1.next=a2
a2.next=a3
b1=ListNode(1)
b2=ListNode(3)
b3=ListNode(4)
b1.next=b2
b2.next=b3
def pri(node):
    while node:
        print(node.val,end="")
        node=node.next
pri(Solution().mergeTwoLists(a1,b1))