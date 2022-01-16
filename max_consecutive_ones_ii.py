from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    left_size = -1
    right_size = 0
    max_size = 0
    for i in nums:
        if i == 0:
            left_size = right_size
            right_size = 0
        else:
            right_size += 1
        max_size = max(max_size, left_size + 1 + right_size)
    return max_size


if __name__ == '__main__':
    a = [1, 0, 1, 1, 0]
    print(findMaxConsecutiveOnes(a) == 4)

    b = [0, 1, 1, 1, 1]
    print(findMaxConsecutiveOnes(b) == 5)

    c = [1, 1, 1, 1, 0]
    print(findMaxConsecutiveOnes(c) == 5)

    d = [1]
    print(findMaxConsecutiveOnes(d) == 1)

    e = [0, 0, 0, 0, 0]
    print(findMaxConsecutiveOnes(e) == 1)

    e = [1, 1, 1, 1, 1]
    print(findMaxConsecutiveOnes(e) == 5)
