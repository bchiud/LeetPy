class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        https://hungqcao.github.io/algorithm/bit-manipulation/2017/08/23/addition-subtraction-using-bit-manipulation.html
        subtraction:
        x | y | x - y | borrow
        1 | 1 |   0   |   0
        1 | 0 |   1   |   0
        0 | 0 |   0   |   0
        0 | 1 |   1   |   1
        
        x - y == x^y
        borrow == ~x&y

        x:  2: 0010 => 0000
        Y: -2: 0010 => 0000
        -----------
            0: 0000

        x:  5: 0101 => 0111 => 0011
        Y: -2: 0010 => 0100 => 0000
        -----------
            3: 0011
        """

        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)

        sign = 1 if a >= 0 else -1

        if a * b >= 0:
            while y > 0:
                x, y = x ^ y, (x & y) << 1
        else:
            while y > 0:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign


if __name__ == '__main__':
    s = Solution()
    assert s.getSum(1, 2) == 3
    assert s.getSum(2, 3) == 5
    assert s.getSum(-10, 5) == -5
    assert s.getSum(5, -10) == -5
    assert s.getSum(-12, -8) == -20
