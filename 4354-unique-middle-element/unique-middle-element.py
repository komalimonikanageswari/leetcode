class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        d = {}
        for i in nums :
            if i in d.keys() :
                d[i] = d[i] + 1 
            else :
                d[i] = 1 
        low = 0 
        high = len(nums) - 1 
        mid = (low+high)//2
        if d[nums[mid]] == 1 :
            return True 
        else :
            return False