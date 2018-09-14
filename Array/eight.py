class Solution:
    """
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums

    # slow
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        cut = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                cut += 1
            else:
                i += 1
            if i + cut >= len(nums):
                break
        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 0, 1, 0]))
    print(Solution().moveZeroes1([0, 1, 1, 0]))