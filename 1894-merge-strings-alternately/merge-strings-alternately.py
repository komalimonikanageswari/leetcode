class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        for i in range(min(len(word1),len(word2))):
            lst.append(word1[i])
            lst.append(word2[i])
        if len(word1) > len(word2) :
            lst.extend(word1[len(word2):])
        elif len(word2) > len(word1) :
            lst.extend(word2[len(word1):])
        return "".join(lst)