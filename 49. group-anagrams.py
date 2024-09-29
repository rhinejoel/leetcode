from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # take each str
        # send to hash Function
        # add hash of each letter and send code back
        # if code in hashmap -> append, add

        a_count = defaultdict(list)
        for s in strs:
            hcode = self.hashFunc(s)
            a_count[hcode].append(s)

        return list(a_count.values())

    def hashFunc(self, str_):
        hcode = 0
        for s in str_:
            hcode += hash(s)
        return hcode