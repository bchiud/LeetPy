from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    longest = 0
    current = 0
    for x in nums:
        if x == 1:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0

    return longest