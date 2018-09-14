import collections


class Solution:
    """
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
    你可以假设字符串只包含小写字母。
    进阶:
    如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

    示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true

    示例 2:
    输入: s = "rat", t = "car"
    输出: false
    """

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        l = []
        for i in range(len(s)):
            if s[i] not in l:
                d[s[i]] = s.count(s[i])
                l.append(s[i])

        for i in range(len(t)):
            if t[i] in d.keys():
                d[t[i]] -= 1
            else:
                return False

        for i, k in d.items():
            if k != 0:
                return False
        return True

    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)

        if len(dic1) != len(dic2):
            return False
        for k,v in dic1.items():
            if k in dic2.keys() and v == dic2[k]:
                continue
            else:
                return False
        return True

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
        # all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False
        return set(s) == set(t) and all(s.count(i) == t.count(i) for i in set(s))


if __name__ == '__main__':
    print(Solution().isAnagram("rat", "cat"))
    print(Solution().isAnagram1("rat", "cat"))
    print(Solution().isAnagram2("anagram", "nagaram"))
