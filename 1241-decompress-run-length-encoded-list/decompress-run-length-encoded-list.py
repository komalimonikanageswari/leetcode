class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            value = nums[2*i+1]
            ans = [value]*freq
            lst += ans
        return lst