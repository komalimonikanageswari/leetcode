class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # n_count = 0
        # for i in range(len(nums)):
        #     count = 0
        #     while(nums[i]>0):
        #         nums[i]=nums[i]//10
        #         count = count+1
        #     if(count%2==0):
        #         n_count = n_count+1
        # return n_count

        count = 0
        for num in nums :
            if len(str(num))%2 == 0 :
                count = count + 1
        return count