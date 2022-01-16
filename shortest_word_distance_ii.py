class WordDistance:

    def __init__(self, wordsDict: List[str]):
        """
        time: n
        space n
        """
        self.locations = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        """
        time: n
        space: 1
        """
        l1, l2 = self.locations[word1], self.locations[word2]
        n1, n2 = len(l1), len(l2)
        i1, i2 = 0, 0
        min_dist = float('inf')

        while i1 < n1 and i2 < n2:
            min_dist = min(min_dist, abs(l1[i1] - l2[i2]))
            if l1[i1] <= l2[i2]:
                i1 += 1
            else:
                i2 += 1

        return min_dist



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)