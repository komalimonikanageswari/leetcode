class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # first window 
        lst = list(blocks)
        opr = 0 
        for i in range(k):
            if lst[i] == "W" :
                opr = opr + 1
        min_count = opr

        # slide window 
        for i in range(k,len(lst)):
            if lst[i-k] == "W" :
                opr = opr - 1
            if lst[i] == "W" :
                opr = opr +  1 
            min_count = min(min_count,opr)
        return min_count       