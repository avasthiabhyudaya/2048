import numpy as np
import random

N = 4  # In response to the question, where we will do 8x8 we can simply replace this by 8, most of the problems will be taken care of by symmetry


class logic:
    def __init__(self):
        self.grid = np.zeros((N, N))

    def __str__(self):
        return str(self.grid)

    def newnumber(self, k=1):
        # grid = np.zeros((N, N))

        empty = list(zip(*np.where(self.grid == 0)))

        for pos in random.sample(empty, k=k):
            if random.random() < 0.2:
                self.grid[pos] = 4  # 20 percent times it will be 4
            else:
                self.grid[pos] = 2

    def movemade(self, move):
        for i in range(N):
            this = self.grid[i, :]  # all columns for this row
            this_n = this[this != 0]

            new_this = np.zeros_like(this)
            new_this[:len(this_n)] = this_n
            self.grid[i, :] = new_this


if __name__ == '__main__':
    game = logic()
    game.newnumber(k=2)
    print(game)
    game.movemade(move='l')
    print(game)
