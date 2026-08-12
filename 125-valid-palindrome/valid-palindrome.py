class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new_string = ""
        # for i in s :
        #     if i.isalnum():
        #         new_string = new_string+i.lower()
        # return new_string == new_string[::-1]

        # Pre-process string (remove special characters , spaces)
        proc_str = ""
        for i in s :
            if i.isalnum():
                proc_str += i.lower()
        # print(proc_str)
        # Apply two pointers on the processed string 
        left,right = 0,len(proc_str)-1
        while left<right :
            if proc_str[left] != proc_str[right]:
                return False
            else :
                left += 1 
                right -= 1 
        return True
