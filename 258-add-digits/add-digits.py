# class Solution:
#     def addDigits(self, num: int) -> int:
#         sum = 0
#         while num>0:
#             digit = num%10
#             sum = sum+digit
#             num = num//10
#             if(num==0 and sum>9):
#                 num = sum
#                 sum = 0
#         return sum

def get_d_sum(n):
    d_sum = 0
    while n>0 :
        r = n%10 
        d_sum = d_sum + r
        n = n//10
    return d_sum
class Solution :
    def addDigits(self,num : int) -> int :
        while True:
            if num<10 :
                break
            num = get_d_sum(num)
        return num 