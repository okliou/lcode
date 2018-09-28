"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 二叉搜索树有特点：左<=根<右
        prev = -float('inf')
        stack = [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]:  # 第1次时,p[1]为root,不为空的时候continue
                continue
            if p[0] == 0:  # p[0]==0时,p[1]为根节点
                if p[1].val <= prev:  # prev用来存储当前节点的前驱节点
                    return False
                prev = p[1].val
            else:
                stack.append((1, p[1].right))  # 1代表左子树或右子树
                stack.append((0, p[1]))  # 0代表根节点
                stack.append((1, p[1].left))
        return True
