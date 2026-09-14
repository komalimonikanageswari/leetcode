class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0 :
            return [0] * n 
        code = code + code
        if k > 0 :
            s = sum(code[1:k+1])
            lst = [s]
            for i in range(1,n):
                s = s + code[i+k] - code[i]
                lst.append(s)
        elif k < 0 :
            k = abs(k)
            s = sum(code[n-k:n])
            lst = [s]
            for i in range(n,2*n-1) :
                s = s + code[i] - code[i-k]
                lst.append(s)
        return lst