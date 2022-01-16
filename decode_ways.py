class Solution:
    def numDecodingsDp(self, s: str) -> int:
        """
        time: n
        space: n
        :param s:
        :return:
        """
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        # none if 0, else 1 way to decode single digit
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            # single digit decoding
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # double digit decoding
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

    def numDecodingsDpConstantSpace(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0

        back_two, back_one = 1, 1
        for i in range(1, n):
            back_two, back_one = back_one, (back_one if s[i] != '0' else 0) \
                                 + (back_two if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)

        return back_one

if __name__ == '__main__':
    s = Solution()

    assert s.numDecodingsDp("12") == 2
    assert s.numDecodingsDp("226") == 3
    assert s.numDecodingsDp("0") == 0
    assert s.numDecodingsDp("06") == 0

    assert s.numDecodingsDpConstantSpace("12") == 2
    assert s.numDecodingsDpConstantSpace("226") == 3
    assert s.numDecodingsDpConstantSpace("0") == 0
    assert s.numDecodingsDpConstantSpace("06") == 0