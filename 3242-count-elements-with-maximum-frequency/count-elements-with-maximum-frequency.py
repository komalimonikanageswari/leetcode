class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = 0 
        d = {}
        for i in nums :
            d[i] = d.get(i,0) + 1 
        lst = []
        max_freq = max(d.values())
        for key,value in d.items() :
            if value == max_freq :
                lst.append(key)
        return len(lst)*max_freq 