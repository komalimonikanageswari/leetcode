class Solution:
    def isValid(self, s: str) -> bool:
        open_b = "({["
        close_b = ")}]"
        st = []
        for i in s :
            # open brackets go into the stack 
            if i in open_b :
                st.append(i)
            else : # when a close bracket is encountered 
                if not st :
                    # if stack is empty then sequence is invalid
                    return False 
                elif i != st[-1] :
                    # check if stack top is corresponding open bracket for this close 
                    if i == ")" and st[-1] == "(" or i == "}" and st[-1] == "{" or i == "]" and st[-1] == "[" :
                        st.pop()
                    else :
                        return False 
        return not st