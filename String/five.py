class Solution:
    """
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为有效的回文串。

    示例 1:
    输入: "A man, a plan, a canal: Panama"
    输出: true

    示例 2:
    输入: "race a car"
    输出: false
    """

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            #   isalnum():检测字符串是否由字母和数字组成
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = 'asdfghjklqwertyuiopzxcvbnm0123456789'
        a = ''
        for i in s.lower():
            if i in t:
                a += i
        return a[::-1] == a

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #   filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
        #   该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
        s = [filter(str.isalnum, s.lower())]
        if s[::-1] == s:
            return True
        return False


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome1("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome2("A man, a plan, a canal: Panama"))
