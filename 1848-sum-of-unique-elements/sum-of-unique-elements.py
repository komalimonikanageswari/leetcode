class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d = {}
        for i in nums :
            if i in d.keys() :
                d[i] += 1 
            else :
                d[i] = 1 
        lst = []
        for key,value in d.items() :
            if value == 1 :
                lst.append(key)
        return sum(lst)