class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        first = {}
        last = {}
        freq = {}
        for i , x in enumerate(nums) :
            if x not in first :
                first[x] = i 
            last[x] = i 
            freq[x] = freq.get(x,0) + 1 
        count = 0 
        for x in freq :
            if last[x] - first[x] == freq[x] - 1 :
                count += 1 
        return count 