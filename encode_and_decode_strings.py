class Codec:

    def encode(self, strs: [str]) -> str:
        """
        Encodes a list of strings to a single string.
        time: n words
        """
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> [str]:
        """
        Decodes a single string to a list of strings.
        time: n words
        """
        ans = []
        i = 0
        while i < len(s):
            next_len = 0
            while s[i] != '#':
                next_len = next_len * 10 + int(s[i])
                i += 1
            i += 1
            ans.append(s[i:i + next_len])
            i += next_len

        return ans


if __name__ == '__main__':
    c = Codec()
    input = ["Hello", "World"]
    assert c.decode(c.encode(["Hello", "World"])) == input



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
