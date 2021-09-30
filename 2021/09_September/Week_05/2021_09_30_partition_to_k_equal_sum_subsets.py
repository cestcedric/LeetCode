class Solution:
    # O(2^n * n) time: in principle try every combination, but with heavy pruning
    # sorting => handle big entries first => buckets always as filled as possible
    # O(n) space: buckets with k < n entries, call stack of depth n
    def canPartitionKSubsets(self, nums: list, k: int) -> bool:
        sumSet = sum(nums)
        sumSubset = sumSet // k

        if sumSubset * k != sumSet or max(nums) > sumSubset: return False

        buckets = [0] * k
        nums.sort(reverse = True)

        def dfs(idx: int):
            nonlocal buckets, nums, sumSubset

            if idx == len(nums): return True

            for b, bucket in enumerate(buckets):
                if bucket == sumSubset: continue
                if bucket + nums[idx] > sumSubset: continue
                if bucket == 0:
                    buckets[b] += nums[idx]
                    if dfs(idx + 1): return True
                    buckets[b] -= nums[idx]
                    break
                
                buckets[b] += nums[idx]
                if dfs(idx + 1): return True
                buckets[b] -= nums[idx]

            return False

        return dfs(0)




testcases = [
    ([4,3,2,3,5,2,1], 4, True),
    ([1,2,3,4], 3, False),
    ([1,1,1,1,2,2,2,2], 4, True),
    ([960,3787,1951,5450,4813,752,1397,801,1990,1095,3643,8133,893,5306,8341,5246], 6, True)
]

for i, (nums, k, target) in enumerate(testcases):
    output = Solution().canPartitionKSubsets(nums, k)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')