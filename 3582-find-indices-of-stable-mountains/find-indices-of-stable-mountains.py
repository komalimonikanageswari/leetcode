class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        lst = []
        for i in range(len(height)-1) :
            if height[i] > threshold :
                lst.append(i+1)
        return lst