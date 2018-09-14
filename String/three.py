class Solution:
    """
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    您可以假定该字符串只包含小写字母。

    s = "leetcode"
    返回 0.

    s = "loveleetcode",
    返回 2.
    """

    # Me (slow)
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:i]:
                return i
        return -1

    #   Not Me (more fast)
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        have_done = []
        for i in range(0, len(s)):
            if s[i] not in have_done:
                if s.count(s[i]) == 1:
                    return i
                else:
                    have_done.append(s[i])
        return -1

    #   Not Me (fastest)
    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm']
        l = []
        for i in range(len(t)):
            if s.count(t[i]) == 1:
                l.append(s.find(t[i]))
        l.sort()
        if len(l) > 0:
            return l[0]
        else:
            return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("loveleetcode"))
    print(Solution().firstUniqChar1("loveleetcode"))
    print(Solution().firstUniqChar2("loveleetcode"))
