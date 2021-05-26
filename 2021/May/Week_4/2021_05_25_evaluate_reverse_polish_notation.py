class Solution:
    def evalRPN(self, tokens: list) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                if t == '+': stack.append(a + b)
                elif t == '-': stack.append(a - b)
                elif t == '*': stack.append(a * b)
                else: stack.append(int(a / b))
            else: stack.append(int(t))
        return stack.pop()


testcases = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().evalRPN(input)
    print('Case #{} should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')
        