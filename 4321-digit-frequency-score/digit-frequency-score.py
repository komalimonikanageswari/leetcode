class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        original = n
        d = {}
        while n > 0 :
            digit = n % 10 
            if digit in d.keys() :
                d[digit] = d[digit] + 1
            else :
                d[digit] = 1
            n = n // 10 
        s = 0 
        for digit , count in d.items() :
            s += digit * count 
        return s