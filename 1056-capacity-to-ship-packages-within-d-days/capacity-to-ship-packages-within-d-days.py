def can_ship(weights,days_have,capacity) :
    # Find the days_needed to ship all the weights under choosen capacity 
    days_needed = 1
    cweights_sum = 0 
    for w in weights :
        if cweights_sum + w <= capacity :
            cweights_sum += w
        else :
            days_needed += 1 
            cweights_sum = w 
    return days_needed <= days_have
    # compare days_needed <= days_have (capacity is a valid choice) 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights) 
        high = sum(weights)
        while low < high :
            mid = (low+high)//2
            if can_ship(weights,days,mid) :
                high = mid 
            else :
                low = mid + 1 
        return low