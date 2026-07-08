from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        ans = True

        for char in s:
            if (char == '(' or char == '{' or char == '['): 
                stack.append(char)
            else:
                if (len(stack) == 0):
                    ans = False
                    break
                else:
                    ele = stack[-1]
                    if (ele == '(' and char == ')'):
                        stack.pop()
                    elif (ele == '{' and char == '}'):
                        stack.pop()
                    elif (ele == '[' and char == ']'):
                        stack.pop()
                    else:
                        ans = False
        
        if (len(stack) > 0):
            ans = False
        
        return ans