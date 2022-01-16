from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l


if __name__ == '__main__':
    s = Solution()
    assert s.peakIndexInMountainArray([0,10,5,2]) == 1
    assert s.peakIndexInMountainArray([3,4,5,1]) == 2
    assert s.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]) == 2