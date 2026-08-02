class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p = nums[i]*nums[j]
                g = math.gcd(nums[i],nums[j])
                strength = p // (g*g)
                ans = max(ans , strength)
        return ans
                