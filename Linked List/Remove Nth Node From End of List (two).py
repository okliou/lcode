"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # fast
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = ListNode(-1)
        l.next = head
        fast = slow = l
        while n and fast.next:
            fast = fast.next
            n -= 1
        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return l.next

    # slow
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) < 2:
            return
        if l[-n].next == None:
            l[-n - 1].next = None
        else:
            l[-n].val = l[-n].next.val
            l[-n].next = l[-n].next.next
        return l[0]
