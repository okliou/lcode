class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

    说明:
    所有输入只包含小写字母 a-z 。
    """

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 1:
            return ""
        i = 0
        j = 0
        end = 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                c = strs[j][i]
            else:
                if strs[j][i] != c:
                    break
            if j == len(strs) - 1:
                i += 1
                j = 0
                end += 1
            else:
                j += 1
        return strs[j][:end]

    # Not Me (fast)
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_len = min([len(i) for i in strs])
        str_ = ''
        for i in range(min_len):
            #   获取列表中各个字符串中同个位置的元素，比较是否相等（set后就只有一个长度）
            if len(list(set([s[i] for s in strs]))) == 1:
                str_ += strs[0][i]
            else:
                return str_
        return str_

    #   Not Me (fastest)
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortstr = min(strs, key=len)
        for i, v in enumerate(shortstr):
            for o in strs:
                if o[i] != v:
                    return shortstr[:i]
        return shortstr


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix1(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix2(["flower", "flow", "flight"]))
