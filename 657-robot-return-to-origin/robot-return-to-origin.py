class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0 
        y = 0
        for s in moves :
            if s == "U" :
                y += 1
            elif s == "R":
                x += 1 
            elif s == "D"  :
                y -= 1 
            else :
                x -= 1 
        if x == 0 and y == 0:
            return True
        else :
            return False