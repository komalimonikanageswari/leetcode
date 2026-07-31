class Solution:
    def countEven(self, num: int) -> int:
        count = 0 
        for i in range(2,num+1):
            sum_ = 0 
            while i > 0 :
                digit = i % 10
                sum_ = sum_ + digit
                i = i//10 
            if sum_ % 2 == 0 :
                count = count + 1
        return count