class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check edge cases of x<0 and x==0
        # Logic remains same for string or list[int]
        # for math logic -> while x>0 append remainder to num and floor divide x by 10
        # reverse num for original order
        
        if x < 0:
            return False
        elif x == 0:
            return True

        # STRING
        # num = str(x)

        # MATH
        num = []
        while x > 0:
            num.append(x % 10)
            x //= 10
        
        num.reverse()

        l, r = 0, len(num)-1
        p = False

        while l <= r:
            if num[l] == num[r]:
                p = True
                if l == r or l+1 == r:
                    return p
            else:
                return False

            l+=1
            r-=1