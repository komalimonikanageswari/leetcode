class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9 + 7 
        s = 0 
        for num in nums :
            width = num % 10 
            d = num // 10 
            digits = len(str(d))
            y_digits = digits - width 
            x = d//(10**y_digits)
            y = d % (10**y_digits)
            s = (s+pow(x,y,mod))%mod
        return s 