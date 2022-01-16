class Solution:
    def countAndSay(self, n: int) -> str:
        s: str = '1'
        if n == 1:
            return s

        for i in range(1, n):
            s = self.helper(s)

        return s

    def helper(self, s: str) -> str:
        curChar = s[0]
        count = 0
        ans = ""
        for i, v in enumerate(s):
            if curChar != v:
                ans += str(count) + str(curChar)

                curChar = v
                count = 1
            else:
                count += 1

        ans += str(count) + str(curChar)

        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.countAndSay(1) == "1"
    assert s.countAndSay(4) == "1211"
