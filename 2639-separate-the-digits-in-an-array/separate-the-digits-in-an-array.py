class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums :
            for digit in str(i):
                lst.append(int(digit))
        return lst