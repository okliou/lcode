class Solution:
    """
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
    你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """

    #   me (timeout)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    l.append([i, j])
        return l

    #   Not Me
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #   不同写法
        # a = {}
        # for i in range(len(nums)):
        #     c = target - nums[i]
        #     if c in a.keys():
        #         print(1)
        #         return [a[c],i]
        #     a[nums[i]] = i

        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum1([2, 7, 11, 15], 9))
