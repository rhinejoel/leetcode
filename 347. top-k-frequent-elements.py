class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ec_map = {}
        freq_map = {}
        bucket = [None]*(len(nums)+1)
        res = []

        for num in nums:
            ec_map[num] = 1 + ec_map.get(num, 0)

        for el, ct in ec_map.items():
            if ct not in freq_map:
                freq_map[ct] = [el]
                bucket[ct] = [el]
            else:
                freq_map[ct].append(el)
                bucket[ct].append(el)
        print(bucket)

        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] != None:
                lb = bucket[i]
                for j in range(len(lb)-1, -1, -1):
                    res.append(lb[j])
                    print(res)
                    if len(res) == k:
                        return res
        