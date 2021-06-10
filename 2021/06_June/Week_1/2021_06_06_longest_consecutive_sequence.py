class Solution:
    # O(n log(n)) time complexity solutions: heapq or sorting and iterating through array
    # in-place sorting pretty quick (since in C) and memory efficient
    # O(n) time complexity => O(1) per element => hash set
    # O(n) space complexity, to save hash table
    def longestConsecutive(self, nums: list) -> int:
        if nums == []: return 0
        setNums = set(nums) # O(n)

        longestSeq = 1
        # O(n)
        for n in setNums:
            if n - 1 not in setNums: # Only start for loop, if n was not yet part of a sequence => avoids O(n^2)
                currentSeq = 1
                currentNum = n
                while currentNum + 1 in setNums:
                    currentSeq += 1
                    currentNum += 1
                longestSeq = max(longestSeq, currentSeq)
        return longestSeq



testcases = [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([], 0),
    ([1], 1)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().longestConsecutive(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')