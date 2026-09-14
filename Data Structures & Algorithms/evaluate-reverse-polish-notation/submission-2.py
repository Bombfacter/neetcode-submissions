class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}

        for char in tokens:
            if char in operators:
                b = stack.pop()
                a = stack.pop()

                if char == "+":
                    num = a + b
                    stack.append(num)
                elif char == "/":
                    num = int(a / b)
                    stack.append(num)
                elif char == "*":
                    num = a * b
                    stack.append(num)
                else:
                    num = a - b
                    stack.append(num)
            else:
                stack.append(int(char))
            
        return stack.pop()