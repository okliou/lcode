class Solution(object):
    """
    将32位整数中的数字进行反转
    ex:
    输入：-123
    输出：-321
    """

    def reverse1(self, x):
        """
        :param x: int
        :return: int
        """
        if x > 2 ** 31 or x < -2 ** 31:
            return 0
        elif x < 0:
            a = (str(0 - x))[::-1]  # int转str再反转
            b = int(a)
            return 0 - b
        else:
            a = (str(x))[::-1]
            b = int(a)
            return b

    # not me
    def reverse(self, x):
        """
        Time:   O(logn) = O(1)
        Space:  O(1)
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.


if __name__ == '__main__':
    print(Solution().reverse1(1233))
    print(Solution().reverse1(-1233))
    print(Solution().reverse(1233))
    print(Solution().reverse(-1233))
