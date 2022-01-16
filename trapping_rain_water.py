from typing import List


class Solution:
    """
    water volume stored at each index is the max height, minus index building height
    time: n
    space: 1
    """
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        volume = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r:
            l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
            if l_max <= r_max:
                volume += l_max - height[l]
                l += 1
            else:
                volume += r_max - height[r]
                r -= 1

        return volume


if __name__ == '__main__':
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([4,2,0,3,2,5]) == 9