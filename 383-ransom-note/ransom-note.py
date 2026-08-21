class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        for i in ransomNote :
            if i in d1.keys() :
                d1[i] += 1 
            else :
                d1[i] = 1
        for j in magazine :
            if j in d2.keys() :
                d2[j] += 1
            else :
                d2[j] = 1
        for item , count  in d1.items() :
            if item not in d2 or d2[item] < count :
                return False 
        return True 