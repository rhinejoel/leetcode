class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # check len of both strings, return false if not equal
        # create value-count map for both strings and check if equal

        s_map = {}
        t_map = {}

        if len(s) != len(t): return False 

        for c in s:
            s_map[c] = 1 + s_map.get(c, 0)

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        if s_map == t_map:
            return True
        else:
            return False