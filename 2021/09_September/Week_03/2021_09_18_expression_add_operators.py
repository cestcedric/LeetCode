class Solution:
    # O(4^n) time: 4 possibilities to combine two digits (mostly)
    # O(4^n) space: same number of possible expressions as above
    def addOperators(self, num: str, target: int) -> list:
        OPERATORS = ['', '+', '-', '*']
        
        num = list(num)
        output = []

        def dfs(expression: str, lastvalue: int, index: int) -> None:
            nonlocal OPERATORS, num, output, target
            
            if index == len(num):
                if eval(expression) == target: output.append(expression)
                return

            for op in OPERATORS:
                if op == '':
                    if lastvalue == 0: continue
                    lastvalue *= 10 + int(num[index])
                else: 
                    lastvalue = int(num[index])
                dfs(expression + op + num[index], lastvalue, index + 1)

        dfs(num[0], int(num[0]), 1)

        return output


testcases = [
    ('123', 6, ['1*2*3','1+2+3']),
    ('232', 8, ['2*3+2','2+3*2']),
    ('105', 5, ['1*0+5','10-5']),
    ('00', 0, ['0*0','0+0','0-0']),
    ('3456237490', 9191, [])
]

for i, (num, target, expected) in enumerate(testcases):
    output = Solution().addOperators(num, target)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, sorted(expected), sorted(output)))
    assert sorted(expected) == sorted(output)
print('All test cases passed')
        