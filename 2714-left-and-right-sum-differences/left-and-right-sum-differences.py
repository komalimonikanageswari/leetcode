class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls = []
        rs = []
        ls.append(0) 
        rs.append(0)
        n = len(nums)
        s = 0 
        for i in range(n-1):
            s = s + nums[i]
            ls.append(s)
        s = 0  
        for j in range(n-1,0,-1):
            s = s + nums[j]
            rs.append(s)
        rs.reverse()
        result = []
        for i in range(n):
            diff = abs(ls[i]-rs[i])
            result.append(diff)
        return result