from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        i, rooms = 0, 0

        for s in starts:
            if s < ends[i]:
                # meeting overlaps, need new room
                rooms += 1
            else:
                # current start and end do not over lap, so check next pair
                i += 1

        return rooms