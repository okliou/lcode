"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    #   TimeOut
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        for i in range(2, n):
            b = []
            for j in range(2, i):
                if i % j == 0:
                    b.append(j)
                    break
            if len(b) == 0:
                a += 1
        return a


if __name__ == '__main__':
    print(Solution().countPrimes(499979))
