class Solution(object):
    """
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    """

    def isPalindrome1(self, x):
        """
        :param x: int
        :return: bool
        """
        if x >= 0:
            a = str(x)
            b = a[::-1]
            if a == b:
                return True
            else:
                return False
        else:
            return False

    # not me
    def isPalindrome(self, x):
        """
        Time:   O(1)
        Space:  O(1)
        :param x: int
        :return: bool
        """
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse


if __name__ == '__main__':
    print(Solution().isPalindrome1(12321))
    print(Solution().isPalindrome1(1231))
    print(Solution().isPalindrome1(-1212))

    print(Solution().isPalindrome(-1212))
    print(Solution().isPalindrome(1212))
    print(Solution().isPalindrome(1221))
