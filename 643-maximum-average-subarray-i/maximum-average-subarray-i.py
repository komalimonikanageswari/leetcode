class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # average of first window 
        window_sum = sum(nums[:k]) 
        average = window_sum / k
        max_average = average 

        # slide window 
        for i in range(k,len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            average = window_sum / k
            max_average = max(max_average,average)

        return max_average 