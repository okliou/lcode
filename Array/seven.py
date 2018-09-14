class Solution:
    """
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。

    输入: [1,2,3]
    输出: [1,2,4]

    输入: [1,2,9]
    输出: [1,3,0]
    """

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = [str(i) for i in digits]
        a = ''.join(d)
        b = int(a) + 1
        c = []
        for i in str(b):
            c.append(int(i))
        return c


if __name__ == '__main__':
    print(Solution().plusOne([1, 2, 3]))
