class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        rep = False
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                rep = True
                break

        return rep