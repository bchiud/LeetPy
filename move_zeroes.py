from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    write_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_pos] = nums[i]
            write_pos += 1

    for i in range(write_pos, len(nums), 1):
        nums[i] = 0


if __name__ == '__main__':
    a = [0, 1, 0, 3, 12]
    moveZeroes(a)
    print(a)
    print(a == [1, 3, 12, 0, 0])

    b = [0]
    moveZeroes(b)
    print(b == [0])
