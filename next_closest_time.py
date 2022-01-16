from collections import Counter


class Solution:
    def nextClosestTime(self, time: str) -> str:
        uniques = Counter(time[:2] + time[3:])

        nums = sorted(uniques.keys())
        n = len(nums)

        if n == 1:
            return time

        m = time[4]
        if nums.index(m) < (n - 1):
            candidate = time[:4] + nums[nums.index(m) + 1]
            if self.isValid(candidate):
                return candidate

        mm = time[3]
        if nums.index(mm) < (n - 1):
            candidate = time[:3] + nums[nums.index(mm) + 1] + nums[0]
            if self.isValid(candidate):
                return candidate

        h = time[1]
        if nums.index(h) < (n - 1):
            candidate = time[:1] + nums[nums.index(h) + 1] + ":" + nums[0] + nums[0]
            if self.isValid(candidate):
                return candidate

        hh = time[0]
        if nums.index(hh) < (n - 1):
            candidate = nums[nums.index(hh) + 1] + nums[0] + ":" + nums[0] + nums[0]
            if self.isValid(candidate):
                return candidate

        return f'{nums[0]}{nums[0]}:{nums[0]}{nums[0]}'

    def isValid(self, time: str) -> bool:
        if time[0:2] >= '24' or time[3:5] >= '60':
            return False;
        return True;


if __name__ == '__main__':
    s = Solution()
    assert s.nextClosestTime("00:00") == "00:00"
    assert s.nextClosestTime("13:55") == "15:11"
    assert s.nextClosestTime("19:34") == "19:39"
    assert s.nextClosestTime("22:55") == "22:22"
    assert s.nextClosestTime("23:59") == "22:22"
