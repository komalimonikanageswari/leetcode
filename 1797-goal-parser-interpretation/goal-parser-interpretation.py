class Solution:
    def interpret(self, command: str) -> str:
        i = 0 
        output = ""
        while i <len(command):
            if command[i] == "G":
                output += "G"
                i = i+1
            elif command[i] == "(":
                if command[i+1] == ")":
                    output += "o"
                    i = i+2 
                else :
                    output += "al"
                    i = i+4
        return output