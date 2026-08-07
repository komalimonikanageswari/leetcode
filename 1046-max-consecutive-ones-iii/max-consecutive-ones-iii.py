class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros_count = 0 
        max_length = 0 
        left = 0 
        for right in range(len(nums)):
            if nums[right] == 0 :
                zeros_count += 1 
        # Find invalid state , until valid shrink the window 
            while zeros_count > k :
                if nums[left] == 0 :
                    zeros_count -= 1 
                left += 1 
        # Update max_length
            max_length = max(max_length, right-left+1)
        return max_length