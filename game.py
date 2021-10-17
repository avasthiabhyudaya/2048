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

    @staticmethod
    def _get_nums(this):
        this_n = this[this != 0]
        this_n_sum = []
        skip = False

        for j in range(len(this_n)):
            if skip:
                skip = False
                continue

            if j != len(this_n) - 1 and this_n[j] == this_n[j+1]:
                new_n = this_n[j] * 2
                if new_n == 2048:
                    exit()
                skip = True

            else:
                new_n = this_n[j]

            this_n_sum.append(new_n)

        return np.array(this_n_sum)

    def movemade(self, move):
        for i in range(N):
            if move in 'lr':
                this = self.grid[i, :]
            else:
                this = self.grid[:, i]

            flipped = False
            if move in 'rd':
                flipped = True
                this = this[::-1]

            this_n = self._get_nums(this)

            new_this = np.zeros_like(this)
            new_this[:len(this_n)] = this_n

            if flipped:
                new_this = new_this[::-1]

            if move in 'lr':
                self.grid[i, :] = new_this
            else:
                self.grid[:, i] = new_this

    def play(self):
        self.newnumber(k=2)
        while True:
            print(self.grid)
            cmd = input()
            if cmd == "q":
                break
            old_grid = self.grid.copy()
            self.movemade(cmd)
            if all((self.grid == old_grid).flatten()):
                continue
            self.newnumber()


if __name__ == '__main__':
    game = logic()
    game.play()
    # game.newnumber(k=2)
    # game.newnumber(k=2)
    # print(game)
    # game.movemade(move='l')
    # print(game)
