import collections
from typing import List


def thirdMax(nums: List[int]) -> int:
    if len(collections.Counter(nums)) < 3:
        return max(nums)

    first = second = third = float('-inf')

    for i in nums:
        if i in (first, second, third):
            pass
        elif i > first:
            first, second, third = i, first, second
        elif i > second:
            second, third = i, second
        elif i > third:
            third = i

    return third


if __name__ == '__main__':
    a = [3, 2, 1]
    print(thirdMax(a) == 1)

    b = [1, 2]
    print(thirdMax(b) == 2)

    c = [2, 2, 3, 1]
    print(thirdMax(c) == 1)

    d = [1, 1, 2]
    print(thirdMax(d) == 2)
