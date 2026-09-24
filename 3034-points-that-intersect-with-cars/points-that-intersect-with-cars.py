class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        diff = [0]*102
        for start , end in nums :
            diff[start] += 1 
            diff[end+1] -= 1 
        curr = 0 
        ans = 0 
        for i in range(1,101):
            curr += diff[i]
            if curr > 0 :
                ans += 1 
        return ans 