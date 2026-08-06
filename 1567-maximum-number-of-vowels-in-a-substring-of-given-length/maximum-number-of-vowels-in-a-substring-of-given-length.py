class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        # vowels in first window 
        for i in range(k):
            if s[i] in "aeiou" :
                count = count + 1
        max_count = count 
        
        # slide window 
        for i in range(k,len(s)):
            if s[i-k] in "aeiou" :
                count = count - 1
            if s[i] in "aeiou" :
                count = count + 1
            max_count = max(max_count,count)
        
        return max_count
            