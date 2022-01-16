class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n > 0:
            if n & 1 == 1:
                ones += 1
            n = n >> 1
        return ones

if __name__ == '__main__':
    s = Solution()
    assert s.hammingWeight(int("00000000000000000000000000001011", 2)) == 3
    assert s.hammingWeight(int("00000000000000000000000010000000", 2)) == 1
    assert s.hammingWeight(int("11111111111111111111111111111101", 2)) == 31