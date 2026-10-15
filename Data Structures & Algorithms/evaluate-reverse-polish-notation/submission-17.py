class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '/', '*']

        result = 0

        for ch in tokens:
            if ch in operators:
                q = stack.pop()
                p = stack.pop()
                if ch == '+' or ch == '-':
                    result = 0
                    
                    if ch == '+':
                        result = p + q
                    else:
                        result = p - q
                    stack.append(result)
                elif ch == '*' or ch == '/':
                    result = 1
                    
                    if ch == '/':
                        result = int(p/q)
                    else:
                        result = p*q

                    stack.append(result)
            else:
                stack.append(int(ch))
        
        return stack.pop()