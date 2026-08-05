class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        m = 1 
        for i in range(2,mx+1):
            if mn%i == 0 and mx%i == 0 and i>m :
                m = i
        return m