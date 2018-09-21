class Solution:
    """
    报数序列是指一个整照其中的整数的顺序进数序列，按行报数，得到下一个数。其前五项如下：

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 被读作  "one 1"  ("一个一") , 即 11。
    11 被读作 "two 1s" ("两个一"）, 即 21。
    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

    给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
    注意：整数顺序将表示为一个字符串。

    示例 1:
    输入: 1
    输出: "1"

    示例 2:
    输入: 4
    输出: "1211"
    """

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1 or n > 30:
            return 0
        a = '1'
        for i in range(n - 1):
            new_a = ''
            j = 0
            while j < len(a):
                count = 1  # 有几个相同的元素
                while j < len(a) - 1 and a[j] == a[j + 1]:
                    j += 1
                    count += 1
                new_a = new_a + str(count) + a[j]
                j += 1
            a = new_a
        return a

    def countAndSay1(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n - 1):
            new_res = ''
            pre = res[0]
            count = 0
            for j in range(len(res)):
                if res[j] == pre:
                    count += 1
                else:
                    new_res = new_res + str(count) + pre
                    pre = res[j]
                    count = 1
            res = new_res + str(count) + pre  # 这里的+str(count)+pre是将最后1个字母的报数加入
        return res


if __name__ == '__main__':
    print(Solution().countAndSay(6))
    print(Solution().countAndSay1(7))
