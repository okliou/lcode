class Solution:
    """
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

    输入: [1,2,3,1]
    输出: true

    输入: [1,2,3,4]
    输出: false
    """
    # Me(最慢)
    def containsDuplicate1(self, nums):
        """
        :param nums: list[int]
        :return:    bool
        """
        for i in range(len(nums)):
            if nums[i] in nums[i + 1:]:
                return True
        return False

    # not me(比较慢)
    def containsDuplicate(self, nums):
        """
        :param nums: list[int]
        :return:    bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    # not me(快)
    def containsDuplicate2(self, nums):
        """
        :param nums: list[int]
        :return:    bool
        """
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    print(Solution().containsDuplicate1([1, 2, 3, 1]))
    print(Solution().containsDuplicate([1, 2, 3, 1]))
    print(Solution().containsDuplicate2([1, 2, 3, 1]))
