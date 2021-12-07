import numpy as np

if __name__ == '__main__':
    file = open('input', 'r')
    positions = np.array(file.read().split(','), dtype=int)
    print("Loaded positions, {} crabs".format(len(positions)))
    moving_costs = []
    for i in range(positions.min(), positions.max()):
        print("Procesing position: {}/{}".format(i, positions.max()))
        target = np.zeros((len(positions),), dtype=int) + i
        deltas = abs(positions-target)
        costs = []
        for element in deltas:
            cost = 0
            for x in range(0, element):
                cost += (1+x)
            costs.append(cost)
        moving_costs.append([i, costs])
    minimum = moving_costs[0]
    for cost in moving_costs:
        if sum(minimum[1]) > sum(cost[1]):
            minimum = cost
    print("Optimal horizontal position: {} using {} units of fuel".format(minimum[0], sum(minimum[1])))
