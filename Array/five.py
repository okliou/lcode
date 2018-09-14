class Solution:
    """
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
    """

    def singleNumber(self, nums):
        """
        :param nums:    list[int]
        :return:    int
        """
        # nums.sort()
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

    # more fast
    def singleNumber1(self, nums):
        """
        :param nums:    list[int]
        :return:    int
        """
        s = 0
        for i in nums:
            s ^= i
        return s


if __name__ == '__main__':
    print(Solution().singleNumber([2, 2, 1]))
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
    print(Solution().singleNumber1([4, 1, 2, 1, 2, 3, 4]))
