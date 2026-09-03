class Solution:
    def frequencySort(self, s: str) -> str:
        lst = []
        d = {}
        for i in s :
            if i in d.keys() :
                d[i] += 1
            else :
                d[i] = 1 
        ans = ""
        sorted_items = sorted(d.items(),key = lambda x : x[1],reverse = True)
        for ch , freq in sorted_items :
            ans += ch * freq
        return ans 
        