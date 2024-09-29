class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a value-index map
        # for each element - calculate required val to meet target
        # if required in vi_map, then return current index and key, else add to map

        vi_map = {}

        for i in range(len(nums)):
            r_val = target - nums[i]
            if r_val in vi_map and r_val == nums[i]:
                return [vi_map[r_val], i]
            elif r_val in vi_map:
                return [vi_map[r_val], i]
            else:
                vi_map[nums[i]] = i