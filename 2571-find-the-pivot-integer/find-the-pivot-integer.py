class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = []
        s = 0 
        for i in range(1,n+1):
            s = s + i 
            prefix_sum.append(s)
        if prefix_sum[0] == prefix_sum[n-1] :
            return n 
        for i in range(1,n) :
            if prefix_sum[i] == prefix_sum[n-1] - prefix_sum[i-1] :
                return i + 1 
        else :
            return -1 