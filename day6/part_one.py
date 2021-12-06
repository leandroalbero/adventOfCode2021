import time
# This way of programming does not scale because its cost is exponential

class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            fishes.append(Lanternfish(9))


fishes = []

if __name__ == '__main__':
    file = open('input', 'r')
    initial_timers = file.read().split(',')
    for fish in initial_timers:
        fishes.append(Lanternfish(int(fish)))
    print("{} fishes loaded! Starting simulation...".format(len(fishes)))
    print(initial_timers)
    start = time.time()
    for i in range(256):
        print("iteration: {} time: {}s fishes: {}".format(i, (time.time()-start),len(fishes)))
        for fish in fishes:
            fish.tick()
        #print("Day {}: {}".format(i,fishes_states))
    print(len(fishes))
