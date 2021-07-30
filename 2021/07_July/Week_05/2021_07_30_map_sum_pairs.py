class Node:
    # O(k) time complexity: k = len(key)
    # O(k) space complexity
    def __init__(self, key, val = 0):
        if key is None or len(key) == 1:
            self.key = key
            self.total = val
            self.val = val
            self.children = []
        else:
            self.key = key[0]
            self.total = val
            self.val = 0
            self.children = [Node(key[1:], val)]
    

    # O(k) time complexity
    # O(k) space complexity: most space needed when prefix completely unknown
    def insert(self, key, val):
        # actually just update existing node
        if self.key == key:
            diff = val - self.val
            self.total += diff
            self.val = val
        # found prefix
        elif self.key == key[0]:
            diff = None
            for c in self.children:
                if c.key == key[1]:
                    diff = c.insert(key[1:], val)
            if diff is None:
                diff = val
                self.children.append(Node(key[1:], val))
            self.total += diff
        # sentinel node
        else:
            diff = None
            for c in self.children:
                if c.key == key[0]:
                    diff = c.insert(key, val)
            if diff is None:
                diff = val
                self.children.append(Node(key, val))
            self.total += diff
        return diff

    
    def printTrie(self):
        print('key: {}\nval: {}\ntotal: {}\nchildren: {}'.format(self.key, self.val, self.total, [c.key for c in self.children]))
        print('---')
        for c in self.children:
            c.printTrie()


class MapSum:
    # O(1) time complexity
    # O(1) space complexity
    def __init__(self):
        self.trie = Node(None)
        
    # O(k) time complexity: k = len(key)
    # O(k) space complexity: at most, when no prefix of key in trie
    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)
        
    # O(p) time complexity: p = len(prefix)
    # O(1) space: duh
    def sum(self, prefix: str) -> int:
        def traverse(node, prefix):
            if node.key == prefix: return node.total
            if node.key is not None and node.key != prefix[0]: return 0
            for c in node.children:
                if prefix[1] == c.key: return traverse(c, prefix[1:])
            return 0
            
        return max(traverse(node, prefix) for node in self.trie.children)


class MapSumDict:
    # O(1) time complexity
    # O(1) space complexity
    def __init__(self) -> None:
        self.data = {}

    
    # O(1) time complexity
    # O(1) space complexity: linear growth of dict with number of key : value pairs
    def insert(self, key: str, val: int) -> None:
        self.data[key] = val


    # O(n * p) time complexity: n key-value pairs, p = len(prefix)
    # O(1) space complexity
    def sum(self, prefix: str) -> int:
        total = 0
        p = len(prefix)
        for entry in self.data:
            if entry[:p] == prefix: total += self.data[entry]
        return total


# Your MapSum object will be instantiated and called as such:
mapSum = MapSumDict()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))         # return 3 (apple = 3)
mapSum.insert("app", 2)
print(mapSum.sum("a"))           # return 5 (apple + app = 3 + 2 = 5)
mapSum.insert("apple", 2)
print(mapSum.sum("ap"))
