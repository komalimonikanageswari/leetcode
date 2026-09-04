class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0 :
            s1 = str(x)
            ans = int(s1[::-1])
        else :
            s2 = str(x//-1)
            ans = int("-"+s2[::-1])
        if ans < -2**31 or ans > 2**31 - 1 :
            return 0 
        return ans