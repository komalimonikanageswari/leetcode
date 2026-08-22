class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0 
        p = 1 
        original = n 
        while n > 0 :
            digit = n % 10 
            s += digit 
            p *= digit 
            n = n // 10 
        result = s + p 
        if original % result == 0 :
            return True 
        else :
            return False 