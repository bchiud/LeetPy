from typing import List


class Solution:
    """
    time: log n
    space: 1
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.helper(nums, target, True)
        if left == -1:
            return [-1, -1]

        right = self.helper(nums, target, False)

        return [left, right]

    def helper(self, nums: List[int], target: int, findLower: bool):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if findLower:
                    if left == mid or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1

            elif nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10], 8) == [3,4]