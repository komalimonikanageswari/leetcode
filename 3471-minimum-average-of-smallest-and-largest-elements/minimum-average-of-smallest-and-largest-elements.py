class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        left = 0 
        right = len(nums) - 1 
        while left < right :
            average = (nums[left] + nums[right]) / 2
            averages.append(average)
            left += 1 
            right -= 1 
        return min(averages) 