from typing import List


class Solution:
    def countBitsCount(self, n: int) -> List[int]:
        return [self.countOnes(i) for i in range(0, n + 1)]

    def countOnes(self, n: int) -> int:
        ones = 0
        while n > 0:
            ones += n & 1
            n >>= 1
        return ones

    def countBitsDp(self, n: int) -> List[int]:
        """
        0: 0000 => 0
        1: 0001 => 1
        2: 0010 => 1
        3: 0011 => 2
        4: 0100 => 1
        5: 0101 => 2
        6: 0110 => 2
        7: 0111 => 3
        8: 1000 => 1

        even: same as count[i // 2]
        odd: 1 + count[i // 2)]
         6: 0110     3: 011
        12: 1100     7: 111
        """
        ans = [0]
        for i in range(1, n + 1):
            if i % 2 == 0:
                ans.append(ans[i // 2])
            else:
                ans.append(1 + ans[i // 2])
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.countBitsCount(2) == [0, 1, 1]
    assert s.countBitsCount(5) == [0, 1, 1, 2, 1, 2]

    assert s.countBitsDp(2) == [0, 1, 1]
    assert s.countBitsDp(5) == [0, 1, 1, 2, 1, 2]
