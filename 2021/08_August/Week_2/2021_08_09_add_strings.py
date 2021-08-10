class Solution:
    charToDigit = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }

    # O(max(len(num1), len(num2))) time
    # O(1) space: not counting answer, else O(max(len(num1), len(num2)))
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0': return num2
        if num2 == '0': return num1

        # cleaner than handling different lengths
        num1 = num1.zfill(len(num2))
        num2 = num2.zfill(len(num1))

        total = []
        carry = 0
        
        for i in range(len(num1) - 1, -1, -1):
            x, y = num1[i], num2[i]
            s = self.charToDigit[x] + self.charToDigit[y] + carry
            total.append(str(s % 10))
            carry = s // 10

        if carry > 0: total.append(str(carry))
        
        total = ''.join(total)

        return total[::-1]


testcases = [
    ('0', '1234', '1234'),
    ('11', '123', '134'),
    ('99', '1', '100')
]

for i, (num1, num2, target) in enumerate(testcases):
    output = Solution().addStrings(num1, num2)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed')