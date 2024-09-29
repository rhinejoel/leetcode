class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Delete in reverse
        l = len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]

        r = l - len(nums)

        nums.extend([0] * r)