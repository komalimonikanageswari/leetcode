class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lst = []
        for i in range(len(arr)-1) :
            for j in range(i+1,len(arr)) :
                lst.append((arr[i]/arr[j],arr[i],arr[j]))
        lst.sort()
        return [lst[k-1][1] , lst[k-1][2]]