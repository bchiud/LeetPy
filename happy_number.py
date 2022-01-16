class Solution:
    def isHappySet(self, n: int) -> bool:
        """
        time: log n => number of digits in a given number
        space: log n => numbers put in hashset
        """
        s = set()

        while n not in s and n != 1:
            s.add(n)

            m = 0
            while n:
                m += (n % 10) ** 2
                n //= 10
            n = m

        return True if n == 1 else False

    def isHappyFloydCycleAlgo(self, n: int) -> bool:
        """
        time: log n => number of digits in a given number
        space: 1
        """
        def next_n(n: int):
            # this takes log n time
            m = 0
            while n:
                m += (n % 10) ** 2
                n //= 10
            return m

        slow, fast = next_n(n), next_n(next_n(n))
        while slow != fast and fast != 1:
            slow = next_n(slow)
            fast = next_n(next_n(fast))
            print(f'slow: {slow}, fast: {fast}')

        return fast == 1


if __name__ == '__main__':
    s = Solution()
    assert s.isHappyFloydCycleAlgo(19) == True
