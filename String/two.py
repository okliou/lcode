class Solution:
    """
    给定一个 32 位有符号整数，将整数中的数字进行反转。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

    示例 1:
    输入: 123
    输出: 321

    示例 2:
    输入: -123
    输出: -321
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 < x < 2**31 - 1:
            if x < 0:
                x = str(0 - x)[::-1]
                if -2**31 < 0 - int(x) < 2**31 - 1:
                    return 0 - int(x)
                else:
                    return 0
            else:
                x = (str(x))[::-1]
                if -2**31 < int(x) < 2**31 - 1:
                    return int(x)
                else:
                    return 0
        else:
            return 0

    #   Not Me(fast)
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])

        return new_x if -2**31 <= new_x <= 2**31 -1 else 0


if __name__ == '__main__':
    print(Solution().reverse(-123))
    print(Solution().reverse1(-123))