class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(k,(len(nums)*k)+1,k):
            if i not in nums :
                return i 
        return i+k