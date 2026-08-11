class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        mx = max(candies)
        for i in candies :
            if mx <= i+extraCandies:
                lst.append(True)
            else:
                lst.append(False)
        return lst 