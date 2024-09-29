class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort intervals
        # iterate through intervals
        # store num[-1] as lastend
        # compare with start value of each pair and replace if less
        # if more, append to output

        intervals.sort(key = lambda pair: pair[0])
        out = [intervals[0]]

        for s, e in intervals[1:]:
            l = out[-1][1]
            if l >= s:
                out[-1][1] = max(l, e)
            else:
                out.append([s, e])
        
        return out