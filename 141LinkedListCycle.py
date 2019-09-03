# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#两种思路，一是快慢指针，二是替换掉节点里头的值为一个不会出现的数字，如果循环到了这个数字，则有环
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while(head):
            if head.val!=None:
                head.val=None
                head=head.next
            else:
                return True
        return False


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=slow=head
        while(True):
            if not fast:
                return False
            slow=slow.next
            fast=fast.next
            if fast:
                fast=fast.next
                if fast==slow:
                    return True












