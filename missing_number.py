from typing import List


class Solution:
    def missingNumberSorted(self, nums: List[int]) -> int:
        """
        time: n log(n)
        space: 1
        """
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i

        return len(nums)

    def missingNumberSet(self, nums: List[int]) -> int:
        """
        time: n
        space: 1
        """
        s = set(nums)
        n = len(nums)
        for i in range(n):
            if i not in s:
                return i

        return n

    def missingNumbersBit(self, nums: List[int]) -> int:
        missing = len(nums)  # set to size. if all is present it will return size, else it will get xor'ed out
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing



if __name__ == '__main__':
    s = Solution()
    assert s.missingNumberSorted([3, 0, 1]) == 2
    assert s.missingNumberSorted([0, 1]) == 2
    assert s.missingNumberSorted([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert s.missingNumberSorted([0]) == 1

    assert s.missingNumberSet([3, 0, 1]) == 2
    assert s.missingNumberSet([0, 1]) == 2
    assert s.missingNumberSet([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert s.missingNumberSet([0]) == 1

    assert s.missingNumbersBit([3, 0, 1]) == 2
    assert s.missingNumbersBit([0, 1]) == 2
    assert s.missingNumbersBit([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert s.missingNumbersBit([0]) == 1
