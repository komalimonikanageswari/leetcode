class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = []
        double = []
        for i in nums :
            if len(str(i)) == 1 :
                single.append(i)
            else :
                double.append(i)
        if sum(single) == sum(double) :
            return False 
        else :
            return True