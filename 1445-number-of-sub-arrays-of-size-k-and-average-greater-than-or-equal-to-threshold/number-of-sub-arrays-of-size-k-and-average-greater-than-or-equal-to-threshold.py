class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # sum of first window 
        window_sum = sum(arr[:k])
        average = window_sum // k
        if average >= threshold :
            count = 1
        else :
            count = 0

        # slide the window 
        for i in range(k,len(arr)):
            window_sum = window_sum - arr[i-k] + arr[i]
            average = window_sum // k
            if average >= threshold :
                count = count + 1
        
        return count