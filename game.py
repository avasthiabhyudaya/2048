import numpy as np
import random


class logic:
    def __init__(self):
        self.grid = np.zeros((N, N))

    N = 4  # In response to the question, where we will do 8x8 we can simply replace this by 8, most of the problems will be taken care of by symmetry

    grid = np.zeros((N, N))

    empty = list(zip(*np.where(self.grid == 0)))

    for pos in random.sample(empty, k=1):
        if random.random() < 0.2:
            self.grid[pos] = 4  # 20 percent times it will be 4
        else:
            self.grid[pos] = 2


if __name__ == '__main__':
    game = logic()
