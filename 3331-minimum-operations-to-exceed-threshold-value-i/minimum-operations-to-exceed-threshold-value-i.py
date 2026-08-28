class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operations = 0 
        i = 0 
        while nums[i] < k :
            operations += 1 
            i += 1 
        return operations