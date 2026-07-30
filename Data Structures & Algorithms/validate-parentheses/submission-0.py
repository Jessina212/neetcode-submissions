class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in pairs:
                #implies this is a closing bracket
                if len(stack) == 0 or stack.pop() != pairs[char]:
                    return False
            
            else:
                #implies this is an opening bracket
                stack.append(char)
        
        return len(stack) == 0