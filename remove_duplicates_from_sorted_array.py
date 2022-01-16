from typing import List


def removeDuplicates(nums: List[int]) -> int:
    left = 0
    right = 1
    size = len(nums)

    while right < size:
        if (nums[left] != nums[right]):
            left += 1
            nums[left] = nums[right]
        right += 1

    return left + 1


if __name__ == '__main__':
    a = [1, 1, 2]
    print(removeDuplicates(a) == 2)
    print(a == [1, 2, 2])

    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(b) == 5)
    print(b == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4])
