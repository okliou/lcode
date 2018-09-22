"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = ListNode(-1)
        b = a
        while l1 and l2:
            if l1.val <= l2.val:
                a.next = l1
                l1 = l1.next
                a = a.next
            else:
                a.next = l2
                l2 = l2.next
                a = a.next
        if l1:
            a.next = l1
        elif l2:
            a.next = l2
        return b.next

    #   Not Me (递归)
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists1(l1.next, l2)
            return l1
        if l2.val < l1.val:
            l2.next = self.mergeTwoLists1(l2.next, l1)
            return l2
