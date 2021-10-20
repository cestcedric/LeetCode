class Solution:
    # O(n) time: n = len(s)
    # O(n) space: create list with split parts of s
    def reverseWords(self, s: str) -> str:
        s = [substring for substring in s.split(' ') if substring != '']
        s.reverse()
        return ' '.join(s)
        