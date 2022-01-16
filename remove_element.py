from typing import List


def removeElement(nums: List[int], val: int) -> int:
    pos = 0
    for x in nums:
        if x != val:
            nums[pos] = x
            pos += 1
    return pos


if __name__ == '__main__':
    a = [3, 2, 2, 3]
    print(removeElement(a, 3) == 2)
    print(a == [2, 2, 2, 3])

    b = [0, 1, 2, 2, 3, 0, 4, 2]
    print(removeElement(b, 2) == 5)
    print(b == [0, 1, 3, 0, 4, 0, 4, 2])
