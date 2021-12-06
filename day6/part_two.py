import time

if __name__ == '__main__':
    file = open('input', 'r')
    initial_timers = file.read().split(',')
    timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in initial_timers:
        timers[int(fish)] += 1
    starting_time = time.time_ns()
    for epoch in range (256):
        temp_timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(timers)):
            if i == 0:
                temp_timers[6] += timers[i]
                temp_timers[8] += timers[i]
            else:
                temp_timers[i-1] += timers[i]
        timers = temp_timers.copy()
    print("result: {}, time: {} ns".format(sum(timers), time.time_ns()-starting_time))
