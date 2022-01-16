class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        time: n^2
        space: n
        """
        n, n_w = len(sequence), len(word)

        if n == 0 or n_w > n:
            return 0

        k = 1
        while word * k in sequence:  # word * k will take n space at most
            k += 1

        return k - 1
