class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # have two vars maxsum and cursum
        # init them equal to nums[0] -> atleast one value then sum is that value
        # iterate through nums

        cursum, maxsum = nums[0], nums[0]

        for num in nums[1:]:
            cursum = max(cursum, 0)
            cursum += num 
            maxsum = max(cursum, maxsum)

        return maxsum