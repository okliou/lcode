"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = []
        b = 0
        while head:
            a.append(head.val)
            head = head.next
            b += 1
        for i in range(b // 2):
            if a[i] != a[-1 - i]:
                return False
        return True

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a[:] == a[::-1]
