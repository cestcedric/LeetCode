import random

class Solution:

    # O(1) time complexity
    # O(n) space complexity: we have to keep the memory for nums obviously
    def __init__(self, nums: list):
        self.nums = nums
        

    # O(1) time complexity
    # O(1) space complexity
    def reset(self) -> list:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    # O(n) time complexity
    # O(n) space complexity: create new list with n elements
    # Fisher-Yates Shuffle
    def shuffle(self) -> list:
        """
        Returns a random shuffling of the array.
        """
        shuffled = [n for n in self.nums]

        for i in range(len(self.nums)):
            r = random.randint(i, len(self.nums))
            shuffled[i], shuffled[r] = shuffled[r], shuffled[i]
        
        return shuffled

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()