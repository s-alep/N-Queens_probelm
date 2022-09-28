import copy
from State import *

visited = []
class HillClimbing:

    def __init__(self, state):
        self.state = state

    def go_to_hill(self):
        return self.climb(self.state, self.state.get_max_score())



    def climb(self, state, prev_score):
        s = state
        if s.score == 0:
            return s

        c = state.get_kids()
        c.sort()

        for i in c:
            for j in visited:
                if(i == j):
                    return 1

            visited.append(i)
            a = self.climb(i, s.score)
            if type(a) == int:
               continue
            if type(a) == State:
              return a


        state.test()
        return 1




