"""
time: 2 ^ n
space: 2 ^ n
"""


def kthGrammarBrute(N: int, K: int) -> int:
    return helperBrute('0', N, K)


def helperBrute(s: str, N: int, K: int) -> int:
    if N == 0:
        return int(s[K - 1])
    new_s = ''
    for i in s:
        # print(i == '0')
        new_s += '01' if i == '0' else '10'
        # print(new_s)
    return helperBrute(new_s, N - 1, K)


"""
time: N
space: N
https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/427711/Python-recursive-solution-No-binary

1 2 3 4 5 6 7 8
0 1 1 0 1 0 0 1

5 (1) and 6 (0) are based off 3 (1)
7 (0) and 8 (1) are based off 4 (0)

odd = odd // 2 + 1
even = even // 2
"""


def kthGrammarParent(N: int, K: int) -> int:
    if N == 1 and K == 1:
        return 0

    # if K is odd, it will be the same as K // 2 + 1
    if K % 2:
        return kthGrammarParent(N - 1, K // 2 + 1)
    # if K is even, it will be the opposite of K // 2
    return 1 - kthGrammarParent(N - 1, K // 2)


"""
N  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6  L = 2^(N - 1)   2^N
5: 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0  16              4
4: 0 1 1 0 1 0 0 1                  8               3
3: 0 1 1 0                          4               2
2: 0 1                              2               1
1: 0                                1               0

time: N
space: N
https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/113736/PythonJavaC++-Easy-1-line-Solution-with-detailed-explanation/304165
"""


def kthGrammarHalf(N: int, K: int) -> int:
    # base case
    if N == 1 and K == 1:
        return 0

    # midpoint of current row is length of previous row
    mid = 2 ** (N - 1) // 2

    # if k is in first half, use previous row
    if K <= mid:
        return int(kthGrammarHalf(N - 1, K))

    # else k is in 2nd half, use opposite of first half
    return int(not kthGrammarHalf(N - 1, K - mid))


if __name__ == '__main__':
    # for i in range(5):
    #     print(f'{i}: {bin(i)}')
    print(kthGrammarParent(1, 1) == 0)
    print(kthGrammarParent(2, 1) == 0)
    print(kthGrammarParent(2, 2) == 1)
    print(kthGrammarParent(4, 5) == 1)

    print(kthGrammarHalf(1, 1) == 0)
    print(kthGrammarHalf(2, 1) == 0)
    print(kthGrammarHalf(2, 2) == 1)
    print(kthGrammarHalf(4, 5) == 1)

    print(kthGrammarBrute(1, 1) == 0)
    print(kthGrammarBrute(2, 1) == 0)
    print(kthGrammarBrute(2, 2) == 1)
    print(kthGrammarBrute(4, 5) == 1)
