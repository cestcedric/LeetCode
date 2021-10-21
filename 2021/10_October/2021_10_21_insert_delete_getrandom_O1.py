import random

# O(1) time on average
# O(n) space used after n insert operations
class RandomizedSet:

    # O(1)
    def __init__(self):
        self.idx = {}
        self.values = []
        

    # O(1): dictionary containing all indexes of values in a list
    # list allows for random index retrieval
    def insert(self, val: int) -> bool:
        if val in self.idx: return False
        self.values.append(val)
        self.idx[val] = len(self.values) - 1
        return True
        

    # O(1): dict check for number in constant time
    # swap last entry with deleted entry for constant time removal
    def remove(self, val: int) -> bool:
        if val not in self.idx: return False
        position = self.idx.pop(val)
        if position != len(self.values) - 1:
            self.values[position] = self.values[-1]
            self.idx[self.values[-1]] = position
        self.values.pop()
        return True
        

    # O(1): use list to be able to access random index
    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()