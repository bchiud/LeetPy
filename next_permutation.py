from typing import List


# def nextPermutation(nums: List[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     1) search from end as long as list is decreasing order
#     2) if entire list is descending order, reverse list
#     3) swap: number prior to "decreasing order" section, and smallest number greater than that in the "decreasing order" section
#     4) reverse "decreasing order" section
#     """
#     if len(nums) <= 1:
#         return
#
#     i = len(nums) - 1
#     while i > 0 and nums[i - 1] >= nums[i]:
#         i -= 1
#
#     if i == 0:
#         nums.reverse()
#         return
#
#     j, k = i - 1, len(nums) - 1
#     while nums[j] >= nums[k]:
#         k -= 1
#     nums[j], nums[k] = nums[k], nums[j]
#
#     l, r = j + 1, len(nums) - 1
#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1

def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    1 2 3 4 2 1 0
    1 2 4 3 2 1 0
    1 2 4 0 1 2 3

    1) find first ascending from back
    2) if no ascending, return reverse
    3) else replace i with smallest number larger than i, and reverse rest of array
    """

    n = len(nums)

    if n < 2:
        return

    # find first ascending from back
    i = n - 2
    while 0 <= i and nums[i] >= nums[i + 1]:
        i -= 1

    # if no ascending, return reverse
    if i == -1:
        nums.reverse()
        return

    # find small number larger than i from right hand side
    j = n - 1
    while nums[i] >= nums[j]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

    # reverse rest of right hand side
    l, r = i + 1, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    return


def checkNextPermutation(nums: List[int], expected: List[int]) -> bool:
    before = nums.copy()
    nextPermutation(nums)
    print(f'results: {nums == expected},   before: {before},   after: {nums},   expected: {expected}')


if __name__ == '__main__':
    # checkNextPermutation([1, 2, 3], [1, 3, 2])
    checkNextPermutation([3, 2, 1], [1, 2, 3])
    checkNextPermutation([1, 3, 2], [2, 1, 3])
    # checkNextPermutation([1, 1, 5], [1, 5, 1])
    checkNextPermutation([1], [1])
    checkNextPermutation([1, 1], [1, 1])
    # checkNextPermutation([1, 2, 4, 3], [1, 3, 2, 4])
    # checkNextPermutation([1, 3, 4, 2], [1, 4, 2, 3])
