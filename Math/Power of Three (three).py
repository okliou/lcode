"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

示例 2:
输入: 0
输出: false

示例 3:
输入: 9
输出: true

示例 4:
输入: 45
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？
"""


class Solution:
    # use math
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        import math
        a = math.log(n, 3)
        return 3 ** math.floor(a) == n and 3 ** math.ceil(a) == n

    #   use loop
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n >= 3:
            if n % 3 != 0: return False
            n = n // 3
        return n == 1


if __name__ == '__main__':
    print(Solution().isPowerOfThree(27))
    print(Solution().isPowerOfThree1(27))
