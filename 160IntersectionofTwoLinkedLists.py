# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headB:
            return None
        if not headA:
            return None
        sa=headA
        sb=headB
        flaga=False
        flagb=False
        if headB is headA:
            return headA
        while (True):
            headA=headA.next
            if not headA and not flaga:
                headA=sb
                flaga=True
            elif not headA:
                headA=None
            headB=headB.next
            if not headB and not flagb:
                headB=sa
                flagb=True
            elif not headB:
                headB=None
            if (headA or headB)==False or headA is headB:
                break
        if (headA or headB) ==False:
            return None
        return headA



a1=ListNode(4)
a2=ListNode(1)
a3=ListNode(8)
a4=ListNode(4)
a5=ListNode(5)
b1=ListNode(5)
b2=ListNode(0)
b3=ListNode(1)
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
b1.next=b2
b2.next=b3
b3.next=a3
print(Solution().getIntersectionNode(a1,a1).val)




