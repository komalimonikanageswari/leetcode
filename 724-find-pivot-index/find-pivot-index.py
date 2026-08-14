class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        sum_ = 0 
        for i in range(len(nums)):
            sum_ += nums[i]
            prefix.append(sum_)
        for i in range(len(nums)):
            left_sum = prefix[i]
            right_sum = prefix[len(nums)]-prefix[i+1]
            if left_sum == right_sum :
                return i 
        return -1