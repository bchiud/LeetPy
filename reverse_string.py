from typing import List


def reverseString(s: List[str]) -> None:
    """
    time: n / 2
    space: n / 2
    """
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)

    # """
    # time: n / 2
    # space: 1
    # """
    # left, right = 0, len(s) - 1
    # while left < right:
    #     s[left], s[right] = s[right], s[left]
    #     left, right = left + 1, right - 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
    print(s == ["o", "l", "l", "e", "h"])

    t = ["H", "a", "n", "n", "a", "h"]
    reverseString(t)
    print(t == ["h", "a", "n", "n", "a", "H"])
