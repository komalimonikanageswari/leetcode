class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] = d[i]+1
            else:
                d[i] = 1
        mx = max(d.values())
        for key,value in d.items():
            if value == mx:
                return key