"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) < 1:
            return head
        if len(l) < 2:
            return l[len(l) - 1]
        for i in range(len(l)):
            if i != len(l) - 1:
                head = l[-i - 1]
                head.next = l[-i - 2]
                head = head.next
            else:
                head.val, head.next = l[-i - 1].val, None
        return l[len(l) - 1]

    #   迭代
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        #   从后往前构建链表
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

    #   递归
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head.next
        n = self.reverseList2(p)
        head.next = None
        p.next = head
        return n
