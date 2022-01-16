class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        time: n
        space: 1
        """
        # N, E, S, W
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x = y = 0
        dir_i = 0

        for c in instructions:
            if c == 'L':
                # e.g. go from N to W
                dir_i = (dir_i + 3) % 4
            elif c == 'R':
                # e.g. go from N to E
                dir_i = (dir_i + 1) % 4
            else:
                x += directions[dir_i][0]
                y += directions[dir_i][1]

        """
        1) returned to original position
        2) if it is not facing north, it will return to 0,0 facing north after 4 cycles
        """
        return (x == 0 and y == 0) or dir_i != 0