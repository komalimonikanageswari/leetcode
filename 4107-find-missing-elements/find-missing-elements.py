class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lst = []
        nums.sort()
        for i in range(len(nums)-1) :
            diff = nums[i+1]-nums[i]
            if diff > 1 :
                for j in range(1,diff):
                    lst.append(nums[i]+j)
        return lst