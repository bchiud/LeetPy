class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.

        time: 1
        space: n
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.

        time: 1
        space: 1
        """
        delta = 1 if player == 1 else -1

        # track move
        self.rows[row] += delta
        self.cols[col] += delta
        if row == col:
            self.diag += delta
        if row + col == self.n - 1:
            self.anti_diag += delta

        # check win condition
        if self.n in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
            return 1
        if -self.n in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
            return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)