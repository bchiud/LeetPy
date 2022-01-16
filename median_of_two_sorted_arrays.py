from typing import List


class Solution:
    """
    time: m + n
    space: m + n
    """
    def findMedianSortedArraysBrute(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2

        i1, i2 = 0, 0

        nums = []

        while i1 < l1 or i2 < l2:
            if i1 == l1:
                while i2 < l2:
                    nums.append(nums2[i2])
                    i2 += 1
            elif i2 == l2:
                while i1 < l1:
                    nums.append(nums1[i1])
                    i1 += 1

            elif i1 < l1 and i2 < l2:
                if nums1[i1] <= nums2[i2]:
                    nums.append(nums1[i1])
                    i1 += 1
                else:
                    nums.append(nums2[i2])
                    i2 += 1

        if l % 2 == 1:
            return nums[l // 2]
        else:
            return (nums[l // 2 - 1] + nums[l // 2]) / 2


    """
    time: log(min(m, n))
    space: log(min(m, n))
    """
    def findMedianSortedArraysLog(self, nums1: List[int], nums2: List[int]) -> float:
        a = 1

if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArraysBrute([1,3], [2]) == 2
    assert s.findMedianSortedArraysBrute([1,2], [3,4]) == 2.5
    assert s.findMedianSortedArraysBrute([0,0], [0,0]) == 0
    assert s.findMedianSortedArraysBrute([], [1]) == 1
    assert s.findMedianSortedArraysBrute([2], []) == 2