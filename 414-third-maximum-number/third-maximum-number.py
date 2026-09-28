class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique=list(set(nums))
        unique.sort(reverse = True)
        if(len(unique)<3):
            return max(unique)
        else:
            return unique[2]
            

            