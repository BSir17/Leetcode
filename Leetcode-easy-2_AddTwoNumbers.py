# -*- coding: utf-8 -*-  
#2.两数相加
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=l1
        s2=l2
        choose=s1
        add=0
        while(l1 or l2):
            if l1:
                d1=l1.val
            else:
                d1=0
                choose=s2
            if l2:
                d2=l2.val
            else:
                d2=0
                choose=s1
            temp=d1+d2+add
            shi=temp//10
            ge=temp%10
            if l1:
                l1.val=ge
                l1=l1.next
            if l2:
                l2.val=ge
                l2=l2.next
            add=shi
        if add!=0:
            s=choose
            while(s.next):
                s=s.next
            s.next=ListNode(add)

        return choose

def printl(node):
    while node:
        print(node.val,end=" ")
        node=node.next

a1=ListNode(3)
a2=ListNode(7)

b1=ListNode(9)
b2=ListNode(2)

a1.next=a2
b1.next=b2

c1=ListNode(5)
d1=ListNode(5)
printl(Solution().addTwoNumbers(a1,b1))