from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1:
            return n

        write = 0
        curChar = chars[0]
        count = 0

        for i, v in enumerate(chars):

            if v != curChar:
                # write char
                chars[write] = curChar
                write += 1
                # write count
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1

                curChar = v
                count = 1

            else:
                count += 1

        # write char
        chars[write] = curChar
        write += 1
        # write count
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1

        return write


if __name__ == '__main__':
    s = Solution()
    s.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
    s.compress(["a"]) == 1
    s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
    s.compress(["a", "a", "a", "b", "b", "a", "a"]) == 6
