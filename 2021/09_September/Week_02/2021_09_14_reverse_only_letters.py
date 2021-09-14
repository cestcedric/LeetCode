from string import ascii_lowercase, ascii_uppercase

class Solution:
    # O(n) time: O(1) lookup in set
    # O(n) space: temporarily use list instead of string
    def reverseOnlyLetters(self, s: str) -> str:
        letters = {c for c in ascii_lowercase + ascii_uppercase}
        s = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] in letters and s[right] in letters:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            if s[left] not in letters: left += 1
            if s[right] not in letters: right -= 1

        return ''.join(s)



testcases = [
    ('ab-cd', 'dc-ba'),
    ('a-bC-dEf-ghIj', 'j-Ih-gfE-dCba'),
    ('Test1ng-Leet=code-Q!', 'Qedo1ct-eeLg=ntse-T!')
]

for i, (s, target) in enumerate(testcases):
    output = Solution().reverseOnlyLetters(s)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All cases passed')