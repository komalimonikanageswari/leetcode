class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        lst = []
        for i in range(n) :
            if n % (i+1) == 0 :
                lst.append(nums[i])
        sq = []
        for i in lst :
            square = i * i
            sq.append(square)
        return sum(sq)
