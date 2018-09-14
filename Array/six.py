import time


class Solution:
    """
    给定两个数组，编写一个函数来计算它们的交集

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [4,9]

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2,2]
    """
    #   暴力法
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            index = -1
            for j in range(len(nums2)):
                if nums2[j] == i:
                    index = j
                    break
            if index != -1:
                res.append(i)
                del nums2[index]
        return res

    #   把数组1转成字典，遍历数组2并对照字典来增删
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        print(map)
        for j in nums2:
            if j in map and map[j] > 0:
                map[j] -= 1
                res.append(j)
        return res

    #  用二分搜索来实现
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums2.sort()
        for i in nums1:
            f, j = self.bSearch(nums2, i)
            if f:
                res.append(i)
                del nums2[j]
        return res

    # 二分搜索
    def bSearch(self, nums, i):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if i == nums[mid]:
                return True, mid
            elif i > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False, 0

    # use collections
    def intersect3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import collections
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())


if __name__ == '__main__':
    print(Solution().intersect([4, 9, 5, 3, 4, 5, 2, 2, 1, 2, 3, 4, 5, 61, 234, 123],
                               [9, 4, 9, 8, 4, 4, 3, 2, 1, 23, 5, 6, 7, 8, 9, 3, 4, 5, 3, 24, 123, 123]))
    print(Solution().intersect2([4, 9, 5, 3, 4, 5, 2, 2, 1, 2, 3, 4, 5, 61, 234, 123],
                                [9, 4, 9, 8, 4, 4, 3, 2, 1, 23, 5, 6, 7, 8, 9, 3, 4, 5, 3, 24, 123, 123]))
    print(Solution().intersect3([4, 9, 5, 3, 4, 5, 2, 2, 1, 2, 3, 4, 5, 61, 234, 123],
                                [9, 4, 9, 8, 4, 4, 3, 2, 1, 23, 5, 6, 7, 8, 9, 3, 4, 5, 3, 24, 123, 123]))
