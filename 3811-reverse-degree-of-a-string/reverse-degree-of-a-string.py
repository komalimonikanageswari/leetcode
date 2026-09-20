class Solution:
    def reverseDegree(self, s: str) -> int:
        lst = []
        for i in range(len(s)) :
            lst.append((123-ord(s[i]))*(i+1))
        return sum(lst)