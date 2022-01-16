from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for i, a in enumerate(nums):
            if target - a in storage:
                return [storage[target - a], i]
            else:
                storage[a] = i


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
