from collections import deque

class Solution:
    # O(10,000) time complexity, as at most 10,000 = 10^n states to try
    # For different sized states: O(n^2 * 10^n) time complexity, with n = number of dials and 10 the numbers of the dials
    # O(10^n) space complexity, at most 10^n states to be saved in 'seen' set
    def openLock(self, deadends: list, target: str) -> int:
        seen = set(deadends) # we also don't want to return to previously visited states, so combine both
        def rotate(state):
            for c in range(len(state)):
                for i in [-1, 1]:
                    yield state[:c] + str((int(state[c]) + i) % 10) + state[c+1:]

        start = '0000'

        if target == start: return 0
        if start in seen: return -1

        queue = deque([(start, 0)])
        seen.add(start)

        while queue:
            state, tries = queue.popleft()
            for s in rotate(state):
                if s == target: return tries + 1
                if s not in seen:
                    queue.append((s, tries + 1))
                    seen.add(s)
        return -1



testcases = [
    (['0201','0101','0102','1212','2002'], '0202', 6),
    (['8888'], '0009', 1),
    (['8887','8889','8878','8898','8788','8988','7888','9888'], '8888', -1),
    (['0000'], '8888', -1)
]

for i, (x, y, target) in enumerate(testcases):
    output = Solution().openLock(x, y)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')