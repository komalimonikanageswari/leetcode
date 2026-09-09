class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix = []
        s = 0 
        for i in range(len(nums)) :
            s = s + nums[i]
            prefix.append(s)
        count = 0 
        for j in range(len(prefix)-1) :
            if (prefix[j] - (prefix[len(prefix)-1]-prefix[j])) % 2 == 0 :
                count += 1 
        return count 