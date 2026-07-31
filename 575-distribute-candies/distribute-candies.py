class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        if len(unique_candies) >= len(candyType)//2 :
            return len(candyType)//2
        else :
            return len(unique_candies)