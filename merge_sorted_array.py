from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while n > 0:
        if m <= 0 or nums1[m - 1] <= nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1 == [1, 2, 2, 3, 5, 6])


    nums3 = [1]
    p = 1
    nums4 = []
    q = 0
    merge(nums3, p, nums4, q)
    print(nums3 == [1])
