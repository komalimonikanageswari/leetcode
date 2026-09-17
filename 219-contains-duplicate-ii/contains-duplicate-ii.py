class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)) :
            if nums[i] in d :
                dist = i - d[nums[i]] 
                if dist <= k :
                    return True 
            d[nums[i]] = i  
        return False 