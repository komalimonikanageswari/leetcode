class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in t :
            d[i] = d.get(i,0) + 1 
        for j in s :
            if j in d :
                d[j] -= 1 
            else :
                d[j] = 1 
        for key , value in d.items() :
            if d[key] > 0 :
                return key 