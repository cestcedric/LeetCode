from collections import defaultdict

class Solution:
    # O(n * s) time: n words of length s
    # O(1) space: constant fingerprint length, not counting output here
    # Actually slower than sorting due to manual traversing of words,
    # but better time complexity than calling word.sort() on every word
    def groupAnagrams(self, strs: list) -> list:
        groups = defaultdict(list)

        for s in strs:
            # faster in practice: groups[tuple(sorted(s))].append(s)
            fingerprint = [0] * 26
            for c in s:
                fingerprint[ord(c) - ord('a')] += 1
            groups['_'.join([str(f) for f in fingerprint])].append(s)

        return groups.values()


testcases = [
    (['eat','tea','tan','ate','nat','bat'], [['bat'],['nat','tan'],['ate','eat','tea']]),
    ([''], [['']]),
    (['a'], [['a']])
]

for i, (strs, target) in enumerate(testcases):
    output = Solution().groupAnagrams(strs)
    sortedOutput = sorted([sorted(group) for group in output])
    sortedTarget = sorted([sorted(group) for group in target])

    print('Case #{}: is\n{}, should be\n{}'.format(i + 1, sortedTarget, sortedOutput))

    assert sortedTarget == sortedOutput
print('All test cases passed!')