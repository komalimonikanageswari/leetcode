class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr :
            if i in d.keys() :
                d[i] += 1 
            else :
                d[i] = 1 
        lst = []
        for i in d.values() :
            lst.append(i)
        return len(lst) == len(set(lst))