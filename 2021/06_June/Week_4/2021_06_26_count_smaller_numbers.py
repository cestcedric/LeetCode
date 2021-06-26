from sortedcontainers.sortedlist import SortedList

class Solution:
    # O(n*log(n)) time complexity: bisect and insertion into sorted list O(log(n))
    # O(n) space complexity: additional sorted list with at most n elements
    def countSmaller(self, nums: list) -> list:
        sortedNums = SortedList()
        output = []

        for n in nums[::-1]:
            index = sortedNums.bisect_left(n)
            sortedNums.add(n)
            output.append(index)
        return output[::-1]



testcases = [
    ([5,2,6,1], [2,1,1,0]),
    ([-1], [0]),
    ([-1,-1], [0,0])
]

for i, (input, target) in enumerate(testcases):
    output = Solution().countSmaller(input)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')