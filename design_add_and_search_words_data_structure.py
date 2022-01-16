class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        time: n
        space: n
        """
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        time: n
        space: n
        """
        return self._dfs(self.root, word)

    def _dfs(self, curr: TrieNode, word: str) -> bool:
        if not word:
            return curr.isWord

        ans = False
        if word[0] == '.':
            for child in curr.nodes.values():
                ans = ans or self._dfs(child, word[1:])
        else:
            if word[0] not in curr.nodes:
                return False
            ans = self._dfs(curr.nodes[word[0]], word[1:])

        return ans



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)