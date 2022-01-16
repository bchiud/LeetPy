from typing import List


class Solution:
    def canReachBfs(self, arr: List[int], start: int) -> bool:
        """
        time: n
        space: n
        """
        n = len(arr)
        q = [start]

        while q:
            i = q.pop(0)
            if arr[i] == 0:
                return True
            elif arr[i] < 0:
                continue

            for j in [i - arr[i], i + arr[i]]:
                if 0 <= j < n:
                    q.append(j)

            arr[i] = -arr[i]

        return False

    def canReachDfs(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReachDfs(arr, start - arr[start]) or self.canReachDfs(arr, start + arr[start])

        return False


if __name__ == '__main__':
    s = Solution()

    assert s.canReachBfs([4, 2, 3, 0, 3, 1, 2], 5) == True
    assert s.canReachBfs([4, 2, 3, 0, 3, 1, 2], 0) == True
    assert s.canReachBfs([3, 0, 2, 1, 2], 2) == False

    assert s.canReachDfs([4, 2, 3, 0, 3, 1, 2], 5) == True
    assert s.canReachDfs([4, 2, 3, 0, 3, 1, 2], 0) == True
    assert s.canReachDfs([3, 0, 2, 1, 2], 2) == False
