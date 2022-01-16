from typing import List


class Solution:
    # 0, 1
    # 00,01,11,10 -> 0,1,3,2
    # 000,001,011,010, 100,101,111,110 -> 0,1,3,2,4,5,7,6

    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]

        if n == 1:
            return ans

        for i in range(1, n):
            base = 2 ** i
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] + base)

        return ans


if __name__ == '__main__':
    s = Solution()

    assert s.grayCode(1) == [0, 1]
    assert s.grayCode(2) == [0, 1, 3, 2]
    assert s.grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4]
