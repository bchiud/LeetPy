class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        count = ""

        for c in s:
            if c.isnumeric():
                # append to count
                count += str(c)
            elif c == '[':
                # push new string and count onto stack
                stack.append(["", int(count)])
                count = ""
            elif c == ']':
                # process last count and string, and append to preceding string
                curStr, curCnt = stack.pop()
                stack[-1][0] += (curStr * curCnt)
            else:
                # add to current string
                stack[-1][0] += c

        return stack[-1][0]


if __name__ == '__main__':
    s = Solution()
    assert s.decodeString("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert s.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
