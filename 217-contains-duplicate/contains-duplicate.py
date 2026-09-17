class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums :
            if i in seen :
                return True
                break
            seen.add(i)
        return False