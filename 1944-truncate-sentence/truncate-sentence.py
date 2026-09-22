class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split()
        result = " ".join(lst[:k])
        return result 