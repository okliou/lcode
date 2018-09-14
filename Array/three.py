class Solution:
    """
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    """

    # 测试不及格（ME）
    def rotate1(self, nums, k):
        """
        :param nums: list[int]
        :param k:   int
        :return:    list[int]
        """

        for i in range(k):
            s = nums[0]
            for j in range(1, len(nums)):
                nums[j], s = s, nums[j]
            nums[0] = s
        return nums

    # not me
    def rotate2(self, nums, k):
        """
        :param nums: list[int]
        :param k:   int
        :return:    list[int]
        """
        if nums:
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k]
        return nums

    # not me
    def rotate(self, nums, k):
        """
        :param nums: list[int]
        :param k:   int
        :return:    list[int]
        """
        if len(nums) == 0 or k == 0:
            return

        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        n = len(nums) - 1
        k = k % len(nums)  # 给出的k可能会大于数组长度，这时候就要对原数组取模
        reverse(0, n - k, nums)
        reverse(n - k + 1, n, nums)
        reverse(0, n, nums)
        return nums


if __name__ == '__main__':
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(Solution().rotate1([1, 2, 3, 4, 5, 6, 7], 3))
    print(Solution().rotate2([1, 2, 3, 4, 5, 6, 7], 3))
