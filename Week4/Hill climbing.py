
from itertools import combinations

print("Shashwat_1BF24CS278")

def cost(state):
    attacks = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1

    return attacks

def get_neighbors(state):
    neighbors = []

    for i, j in combinations(range(4), 2):
        new_state = list(state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        neighbors.append(tuple(new_state))

    return neighbors

def hill_climbing(state):
    while True:
        current_cost = cost(state)

        print("\nCurrent State:", state)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("Goal reached!")
            return state

        neighbors = get_neighbors(state)

        for neighbor in neighbors:
            print("Neighbor:", neighbor, "Cost:", cost(neighbor))

        best = min(neighbors, key=cost)

        if cost(best) >= current_cost:
            print("No better neighbor found.")
            return state

        print("Selected Neighbor:", best)
        state = best

initial_state = (3, 1, 2, 0)

solution = hill_climbing(initial_state)

print("\nFinal Solution:", solution)
print("Final Cost:", cost(solution))
