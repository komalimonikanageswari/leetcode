class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = -1 
        lst = []
        for num in nums :
            s = 0 
            while num > 0 :
                digit = num % 10 
                s = s + digit 
                num = num // 10
            lst.append(s)
        for i in range(len(lst)) :
            if lst[i] == i :
                ans = i 
                break
        return ans