class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = []
        result = []
        d = {}
        for i in nums :
            if i in d.keys():
                d[i] = d[i] + 1 
            else :
                d[i] = 1 
        items = sorted(d.items(),key = lambda x : x[1],reverse = True)
        for i in range(k) :
            lst.append(items[i][0])
        return lst