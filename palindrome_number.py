class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        time: log10(n)
        space: 1
        """
        if x < 0:
            return False
        if x // 10 == 0:
            return True

        flipped = 0
        copy = x
        while copy:
            n = copy % 10
            copy = copy // 10
            flipped = flipped * 10 + n

        return flipped == x