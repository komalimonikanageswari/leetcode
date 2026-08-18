class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int: 
        lst = []
        for sentence in sentences :
            lst.append(len(sentence.split()))
        return max(lst)