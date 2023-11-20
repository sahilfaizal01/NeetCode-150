class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        look = {'}':'{',')':'(',']':'['}

        for char in s:
            if char in look.values():
                stack.append(char)
            elif stack and look[char]==stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
