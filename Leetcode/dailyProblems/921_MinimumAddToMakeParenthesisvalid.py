class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        for ch in s:
            if ch == "(":
                stack.append("(")
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
        
        return len(stack)
            



class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        close = 0

        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            elif open > 0:
                open -= 1
            else:
                close +=1
        return open + close

