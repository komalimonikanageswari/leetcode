class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Step - 1 : compute the frequencie of string p 
        d2 = {}
        for i in p :
            d2[i] = d2.get(i,0) + 1
        # Step - 2 : do a p-length sliding window on a count s 
        # count the frequencies of charaters into d1
        k = len(p)
        d1 = {}
        left = 0 
        ans = []
        for right in range(len(s)):
            d1[s[right]] = d1.get(s[right],0) + 1
            if right >= k-1 :
                if d1 == d2 :
                    ans.append(left)
            # Removing the outgoing element 
                d1[s[left]] -= 1 
                if d1[s[left]] == 0 :
                    d1.pop(s[left])
                left += 1 
        return ans