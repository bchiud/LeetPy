def lengthOfLongestSubstring(s: str) -> int:
    """
    time: 2n
    space: min(len(s), 128) -> 128 possible ascii characters
    """
    # max_len = 0
    # size = len(s)
    # storage = set()
    #
    # i, j = 0, 0
    # while j < size:
    #     if storage.__contains__(s[j]):
    #         while s[i] != s[j] and i < j:
    #             storage.remove(s[i])
    #             i += 1
    #         i += 1
    #     else:
    #         storage.add(s[j])
    #
    #     max_len = max(max_len, j - i + 1)
    #     # print(f'i: {i} j: {j}')
    #     j += 1
    #
    # return max_len

    """
    time: n
    space: min(len(s), 128) -> 128 possible ascii characters
    """
    # max_len = 0
    # size = len(s)
    # storage = [None] * 128
    #
    # i, j = 0, 0
    # while j < size:
    #     last_index = storage[ord(s[j])]
    #
    #     if last_index is not None and last_index >= i and last_index < j:
    #         i = last_index + 1
    #
    #     max_len = max(max_len, j - i + 1)
    #     # print(f'i: {i} j: {j}')
    #     storage[ord(s[j])] = j
    #     j += 1
    #
    # return max_len

    """
    time: n
    space: min(m, n) -> where m is # of possible unique characters
    """
    if s == "":
        return 0

    l, r, n, ans = 0, 0, len(s), 0

    last_index = {}

    while r < n:
        if s[r] in last_index:
            l = max(l, last_index[s[r]] + 1)

        ans = max(ans, r - l + 1)

        last_index[s[r]] = r

        r += 1

    return ans


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb") == 3)
    print(lengthOfLongestSubstring("bbbbb") == 1)
    print(lengthOfLongestSubstring("pwwkew") == 3)
    print(lengthOfLongestSubstring("tmmzuxt") == 5)
