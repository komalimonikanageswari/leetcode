class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = [] 
        for ch in s :
            if ch in "aeiouAEIOU" :
                lst.append(ch)
        n = len(lst)
        lst.reverse()
        lst2 = list(s)
        j = 0 
        for i in range(len(lst2)) :
            if lst2[i] in "aeiouAEIOU" :
                lst2[i] = lst[j]
                j += 1 
        return "".join(lst2)
