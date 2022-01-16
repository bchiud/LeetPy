from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # TODO:
        colL, colR = 0, len(mat)