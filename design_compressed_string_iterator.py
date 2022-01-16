class StringIterator:

    """
    time: 1 in most cases, but n if most of the string is numeric
    space: n => input length
    """
    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.n = len(compressedString)
        self.remaining = self._extract_numeric(compressedString, 1)
        self.index = 0

    """
    time: 1 in most cases, but n if most of the string is numeric
    """
    def next(self) -> str:
        if not self.hasNext():
            return " "

        char = self.compressedString[self.index]
        self.remaining -= 1

        if self.remaining == 0:
            self.index += 1
            while self.index < self.n and not self.compressedString[self.index].isalpha():
                self.index += 1

            self.remaining = self._extract_numeric(self.compressedString, self.index + 1)

        return char

    """
    time: 1
    """
    def hasNext(self) -> bool:
        return self.index < self.n

    """
    time: 1 in most cases, but n if most of the string is numeric
    """
    def _extract_numeric(self, s: str, i: int) -> int:
        num = 0
        while i < len(s) and s[i].isnumeric():
            num = num * 10 + int(s[i])
            i += 1
        return num


if __name__ == '__main__':
    s = StringIterator("L1e2t1C1o1d1e1")
    assert s.next() == 'L'
    assert s.next() == 'e'
    assert s.next() == 'e'
    assert s.next() == 't'
    assert s.next() == 'C'
    assert s.next() == 'o'
    assert s.next() == 'd'
    assert s.next() == 'e'
