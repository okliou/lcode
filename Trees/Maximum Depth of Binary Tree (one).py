"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #   BFS(广度优先搜索算法)，用队列
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        depth = 0
        q = [root]
        while len(q) != 0:
            depth += 1
            for i in range(0, len(q)):
                if q[0].right:
                    q.append(q[0].right)
                if q[0].left:
                    q.append(q[0].left)
                print(q)
                del q[0]
        return depth

    #   递归
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        return 1 + max(self.maxDepth1(root.left), self.maxDepth1(root.right))
