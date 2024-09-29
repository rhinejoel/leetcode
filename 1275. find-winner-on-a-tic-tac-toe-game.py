class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        # only count elements of rows, cols and diags
        n = 3
        rows, cols = [0]*n, [0]*n
        d1, d2 = 0, 0
        p = 1

        for r, c in moves:
            rows[r] += p
            cols[c] += p
            if r == c: d1+=p
            if r+c == n-1: d2+=p

            if abs(rows[r])==n or abs(cols[c])==n or abs(d1)==n or abs(d2)==n:
                if p==1:
                    return "A"
                else:
                    return "B"

            p *= -1
        
        if len(moves) == n*n:
            return "Draw"
        else:
            return "Pending"