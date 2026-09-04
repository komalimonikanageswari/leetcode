class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(len(nums1)) :
            target = nums1[i]
            low = 0 
            high = len(nums2) - 1 
            while low <= high :
                mid = (low+high)//2
                if nums2[mid] == target :
                    return target 
                elif nums2[mid] < target :
                    low = mid + 1 
                else :
                    high = mid - 1 
        return -1 