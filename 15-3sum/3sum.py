class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set = set()
        nums.sort()
        for i in range(len(nums)):
            left = i + 1 
            right = len(nums)-1
            while left < right :
                t_sum = nums[i] + nums[left] + nums[right] 
                if t_sum > 0 :
                    right -= 1 
                elif t_sum < 0 :
                    left += 1 
                else :
                    result_set.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1 
        return [list(triplet) for triplet in result_set]