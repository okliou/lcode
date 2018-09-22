"""
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    #   快慢指针法，要是环状的话，快指针和慢指针一定会相遇，空间复杂度为O(1)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        f = s = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False

    #   顺序遍历，边添加边判断是否在字典中，空间复杂度O(n)
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = {}
        while head:
            if id(head) in d:
                return True
            else:
                d[id(head)] = True
            head = head.next
        return False
