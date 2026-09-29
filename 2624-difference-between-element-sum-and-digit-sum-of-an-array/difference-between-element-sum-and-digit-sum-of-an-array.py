class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        lst = []
        for num in nums :
            while num > 0 :
                digit = num % 10 
                lst.append(digit)
                num = num // 10 
        digit_sum = sum(lst)
        return abs(element_sum - digit_sum)