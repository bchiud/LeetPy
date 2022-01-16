from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    time: n
    space: n
    """
    # hashmap: dict = {}
    #
    # for i, a in enumerate(nums):
    #     remaining = target - a
    #     if remaining in hashmap:
    #         return [hashmap.get(remaining), i]
    #     else:
    #         hashmap[a] = i

    """
    time: n log(n)
    space: 1
    """
    nums = enumerate(nums)
    nums = sorted(nums, key=lambda x: x[1])
    i, j = 0, len(nums) - 1
    while i < j:
        cur = nums[i][1] + nums[j][1]
        if cur == target:
            return [nums[i][0], nums[j][0]]
        elif(cur < target):
            i += 1
        else:
            j -= 1


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9) == [0, 1])
    print(twoSum([3, 2, 4], 6) == [1, 2])
    print(twoSum([3, 3], 6) == [0, 1])
