class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) <= 1 :
            return len(nums)
        max_ = max(nums)
        min_ = min(nums)
        max_index = nums.index(max_)
        min_index = nums.index(min_)
        left = min(max_index,min_index)
        right = max(max_index,min_index)
        front = right + 1 
        back = len(nums) - left 
        both = (left+1)+(len(nums)-right)
        return min(front,back,both)