class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right+1):
            temp = i
            is_self_dividing = True
            while temp>0:
                digit = temp%10
                if(digit == 0 or i%digit!=0):
                    is_self_dividing = False
                    break
                temp = temp//10
            if is_self_dividing:
                result.append(i)
        return result       