from HillClimbing import *
import time


def main():
    key = input("Give me the number of queens: ")
    n = int(key)
    state = State(n, 1)
    hill = HillClimbing(state)
    t1 = time.time()
    a = hill.go_to_hill()
    t2 = time.time()
    if type(a) == int:
        print("No solutions found")
    if type(a) == State:
        print("Found solution!")
        a.test()
        print(t2-t1, " sec")


if __name__ == '__main__':
    main()
