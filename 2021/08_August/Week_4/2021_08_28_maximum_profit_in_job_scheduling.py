class Solution:
    def jobScheduling(self, startTime: list, endTime: list, profit: list) -> int:
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort()

        startTime = [job[0] for job in jobs]

        # TODO:

        


testcases = [
    ([1,2,3,3], [3,4,5,6], [50,10,40,70], 120),
    ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150),
    ([1,1,1], [2,3,4], [5,6,4], 6)
]

for i, (startTime, endTime, profit, target) in enumerate(testcases):
    output = Solution().jobScheduling(startTime, endTime, profit)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')