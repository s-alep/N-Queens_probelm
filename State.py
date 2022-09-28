import random
import copy


class State:

    def __init__(self, n, r):
        if type(n) == int:
            if(n <= 3):
                print("ERROR: N must be >3")
                quit()

            self.n = n
            self.array = []

            temp = []

            if r == 0:
                for i in range(n):
                    for j in range(n):
                        if i == 0:
                            temp.append(1)
                        else:
                            temp.append(0)
                    self.array.append(temp)
                    temp = []
            elif r == 1:
                for i in range(n):
                    for j in range(n):
                        temp.append(0)
                    self.array.append(temp)
                    temp = []
                for i in range(n):
                    a = random.randint(0,self.n-1)
                    self.array[a][i] = 1

            # for i in self.array:
            #    print(i)
            self.score = self.evaluate_state()
            if self.score == -1:
                print("Out of bounds Exception")
            # print(self.score)
        elif type(n) == State:
            self.array = copy.deepcopy(n.array)
            self.n = n.n
            self.score = n.score
        else:
            print("ERROR")

    def test(self):

        for i in self.array:
            print(i)

    def get_kids(self):
        d = self.n

        children = []
        for i in range(d):
            for j in range(d):
                if self.array[i][j] == 1:
                    continue
                else:
                    x = State(self, 1)
                    x.move(i, j)
                    children.append(x)
                    del x

        return children

    def evaluate_state(self):
        n = self.n
        score = 0
        for i in range(n):
            for j in range(n):
                if self.array[i][j] == 1:
                    temp = self.evaluate(i, j)
                    if temp == -1:
                        return -1
                    score += temp

        return score

    def evaluate(self, row, col):
        score = 0
        n = self.n
        if (row < 0) | (row >= n) | (col < 0) | (col >= n):
            return -1

        # check lines for threats
        for i in range(self.n):
            if (self.array[row][i] == 1) & (i != col):
                score += 1

        # check diagonals

        # top right
        temp_row = row
        temp_col = col
        while (temp_row != -1) & (temp_col != n ):

            if (self.array[temp_row][temp_col] == 1) & (temp_row != row) & (temp_col != col):
                score +=1
            temp_row -=1
            temp_col +=1

        # top left
        temp_row = row
        temp_col = col
        while (temp_row != -1) & (temp_col != -1):
            if (self.array[temp_row][temp_col] == 1) & (temp_row != row) & (temp_col != col):
                score += 1
            temp_row -= 1
            temp_col -= 1

        # bottom right
        temp_row = row
        temp_col = col
        while (temp_row != n) & (temp_col != n):
            if (self.array[temp_row][temp_col] == 1) & (temp_row != row) & (temp_col != col):
                score += 1
            temp_row += 1
            temp_col += 1

        # bottom left
        temp_row = row
        temp_col = col
        while (temp_row != n) & (temp_col != -1):
            if (self.array[temp_row][temp_col] == 1) & (temp_row != row) & (temp_col != col):
                score += 1
            temp_row += 1
            temp_col -= 1

        return score

    def move(self, i, j):
        for a in range(self.n):
            self.array[a][j] = 0

        self.array[i][j] = 1
        self.score = self.evaluate_state()

    def get_max_score(self):
        return self.n * (self.n-1) +1

    def __eq__(self, other):
        if self.score != other.score:
            return 0
        else:
            return self.array == other.array

    def __gt__(self, other):
        return (self.score > other.score)

    def __lt__(self, other):
        return (self.score < other.score)

    def __ge__(self, other):
        return self.score >= other.score

    def __le__(self, other):
        return self.score <= other.score


