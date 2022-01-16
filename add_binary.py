class Solution:
    """
    time: max(n, m)
    space: max(n, m)
    """

    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        ans = []
        carry = 0
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            carry //= 2

        if carry == 1:
            ans.append('1')

        ans.reverse()
        return ''.join(ans)

    def addBinaryBitManipulation(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            # 1 if 1+0 or 0+1, 1 if 1+1 and then carry
            x, y = x ^ y, ( x & y) << 1

        return bin(x)[2:]


if __name__ == '__main__':
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"

    assert s.addBinaryBitManipulation("11", "1") == "100"
    assert s.addBinaryBitManipulation("1010", "1011") == "10101"
