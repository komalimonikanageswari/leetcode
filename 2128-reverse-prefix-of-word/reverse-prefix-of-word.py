class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word :
            return word
        else :
            for i in range(len(word)):
                if ch == word[i]:
                    return (word[i::-1]+word[i+1:len(word)])