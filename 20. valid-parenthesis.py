class Solution(object):
    def isValid(self, s):
        open = []
        for e in range (len(s)):
            if s[e] in "[{(": open.append(s[e])
            if s[e] in "]})":
                if e==0 or len(open)==0: return False
                else:
                    if open[-1]+s[e] == "[]": open.pop(-1)
                    elif open[-1]+s[e] == "{}": open.pop(-1)
                    elif open[-1]+s[e] == "()": open.pop(-1)
                    else: return False
        if len(open)==0: return True
        else: return False