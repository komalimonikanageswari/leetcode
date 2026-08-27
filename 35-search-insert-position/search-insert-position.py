class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) -1 
        ans = -1 
        while low <= high :
            mid = (low+high)//2 
            if nums[mid] == target :
                ans = mid  
                break
            elif nums[mid] < target :
                low = mid + 1 
            elif nums[mid] > target :
                high = mid -1 
        if ans == -1 :
            if target < nums[0] :
                ans = 0 
            for i in range(len(nums)) :
                if nums[i] < target :
                    ans = i+1 
        return ans 