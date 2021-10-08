class Trie:
    # O(1)
    def __init__(self):
        self.data = {}
        self.isEnd = False


    # O(n) time: n = len(word)
    # O(n) space: if no part of word already in trie, create n new nodes
    def insert(self, word: str) -> None:
        if word == '': 
            self.isEnd = True
            return
        if word[0] not in self.data: self.data[word[0]] = Trie()
            
        self.data[word[0]].insert(word[1:])
        

    # O(n) time: traverse whole word
    # O(n^2) space: call stack depth, also creating new strings
    # reduce to O(n) by using an internal method that traverses word by index
    def search(self, word: str) -> bool:
        if word == '': return self.isEnd
        if word[0] not in self.data: return False
        return self.data[word[0]].search(word[1:])
        

    # O(n) time: traverse whole prefix
    # O(n^2) space: same as for search()
    def startsWith(self, prefix: str) -> bool:
        if prefix == '': return True
        if prefix[0] not in self.data: return False
        return self.data[prefix[0]].startsWith(prefix[1:])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)