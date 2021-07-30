class Node:
    # O(k) time complexity: k = len(key)
    # O(k) space complexity
    def __init__(self, key, val = 0):
        if key is None or len(key) == 1:
            self.key = key
            self.total = val
            self.val = val
            self.children = {}
        else:
            self.key = key[0]
            self.total = val
            self.val = 0
            self.children = {key[1]: Node(key[1:], val)}
    

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
            if key[1] in self.children:
                diff = self.children[key[1]].insert(key[1:], val)
            else:
                diff = val
                self.children[key[1]] = Node(key[1:], val)
            self.total += diff
        # sentinel node
        else:
            if key[0] in self.children:
                diff = self.children[key[0]].insert(key, val)
            else:
                diff = val
                self.children[key[0]] = Node(key, val)
            self.total += diff
        return diff

    
    def printTrie(self):
        print('key: {}\nval: {}\ntotal: {}\nchildren: {}'.format(self.key, self.val, self.total, [self.children[c].key for c in self.children]))
        print('---')
        for c in self.children:
            self.children[c].printTrie()


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
            if prefix == '' or prefix == node.key: return node.total
            if prefix[0] == node.key:
                prefix = prefix[1:]
            if prefix[0] in node.children: 
                return traverse(node.children[prefix[0]], prefix)
            return 0
            
        return traverse(self.trie, prefix)


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
mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))         # return 3 (apple = 3)
mapSum.insert("app", 2)
print(mapSum.sum("a"))           # return 5 (apple + app = 3 + 2 = 5)
mapSum.insert("apple", 2)
print(mapSum.sum("ap"))
