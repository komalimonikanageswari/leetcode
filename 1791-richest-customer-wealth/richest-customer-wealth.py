class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0 
        max_total = 0 
        for row in accounts :
            total = sum(row) 
            max_total = max(max_total,total)
        return max_total