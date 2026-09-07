class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0]
        sum_ = 0 
        for i in range(len(gain)) :
            sum_ += gain[i]
            lst.append(sum_)
        return max(lst)