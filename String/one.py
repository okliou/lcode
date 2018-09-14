class Solution:
    """
    编写一个函数，其作用是将输入的字符串反转过来。
    输入: "hello"
    输出: "olleh"
    """
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    print(Solution().reverseString("hello,abb"))