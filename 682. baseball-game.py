class Solution(object):
    def calPoints(self, ops):
        rec=[]
        for i in range (0, len(ops)):
            if not ops[i] in ['+','C','D']:
                rec.append(int(ops[i]))
            if ops[i] == "+":
                if rec[-2]:
                    rec.append(rec[-1]+rec[-2])
                else:
                    rec.append(rec[-1])
            if ops[i] == "D":
                rec.append(rec[-1] * 2)
            if ops[i] == "C":
                rec.pop(-1)

        return sum(rec)