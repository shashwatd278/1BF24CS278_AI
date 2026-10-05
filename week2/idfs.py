def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    if row > 0:
        new_state = list(state)
        new_state[zero], new_state[zero - 3] = \
            new_state[zero - 3], new_state[zero]
        neighbors.append(tuple(new_state))

    if row < 2:
        new_state = list(state)
        new_state[zero], new_state[zero + 3] = \
            new_state[zero + 3], new_state[zero]
        neighbors.append(tuple(new_state))

    if col > 0:
        new_state = list(state)
        new_state[zero], new_state[zero - 1] = \
            new_state[zero - 1], new_state[zero]
        neighbors.append(tuple(new_state))

    if col < 2:
        new_state = list(state)
        new_state[zero], new_state[zero + 1] = \
            new_state[zero + 1], new_state[zero]
        neighbors.append(tuple(new_state))

    return neighbors

def dls(state, goal, depth, path, visited):

    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for next_state in get_neighbors(state):

        if next_state not in visited:

            result = dls(
                next_state,
                goal,
                depth - 1,
                path + [next_state],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


def ids(initial, goal):

    depth = 0

    while True:

        visited = set()

        result = dls(
            initial,
            goal,
            depth,
            [initial],
            visited
        )

        if result is not None:
            return result

        depth += 1


def print_state(state):

    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])

    print()


initial = (
     1, 2, 3,
    5, 0, 6,
    4, 7, 8
)

goal = (
      1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

path = ids(initial, goal)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)
    print()

    for i, state in enumerate(path):

        print("Step", i)
        print_state(state)

else:

    print("No solution found")