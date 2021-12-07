import numpy as np

if __name__ == '__main__':
    file = open('input', 'r')
    positions = np.array(file.read().split(','), dtype=int)
    print("Loaded positions, {} crabs".format(len(positions)))
    moving_costs = []
    for i in range(positions.min(), positions.max()):
        target = np.zeros((len(positions),), dtype=int) + i
        moving_costs.append([i, abs(positions - target)])
    min = moving_costs[0]
    for cost in moving_costs:
        if sum(min[1]) > sum(cost[1]):
            min = cost
    print("Optimal horizontal position: {} using {} units of fuel".format(min[0], sum(min[1])))
