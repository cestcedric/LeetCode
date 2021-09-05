class Solution:
    # O(n^2) time
    # O(n) space
    # k >= 2: we can switch two entries in order
    # => bubble sort style sorting possible
    # k == 1: only can rotate string, find smallest rotation
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1: return ''.join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))