class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        index = -1 
        for i in range(len(nums)) :
            max_element = max(nums[:i+1])
            min_element = min(nums[i:])
            instability_score = max_element - min_element 
            if instability_score <= k :
                index = i 
                break
        return index 