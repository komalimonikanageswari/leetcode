class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        original = x
        while x>0:
            digit = x%10
            sum = sum+digit
            x = x//10
        if(original%sum==0):
            return sum
        else:
            return -1
        # return sum if original%sum == 0 else -1 