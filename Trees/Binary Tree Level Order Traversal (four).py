"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #   用广度优先搜索算法(BFS)
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        q = [root]
        a = [[root.val]]
        while len(q) != 0:
            b = []
            for i in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                    b.append(q[0].left.val)
                if q[0].right:
                    q.append(q[0].right)
                    b.append(q[0].right.val)
                del q[0]
            a.append(b)
        a.pop()
        return a
