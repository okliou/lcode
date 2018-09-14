class Solution:
    """
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    """

    def removeDuplicates(self, nums):
        """
        :param nums:    list[int]
        :return:    int
        """
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                # slow += 1 # 运行速率比下面的略慢
                slow = slow + 1
                nums[slow] = nums[i]
        return slow + 1


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2, 3]))
