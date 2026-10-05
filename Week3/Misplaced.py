def misplaced_tiles(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def get_successors(state):
    successors = []
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(blank - 3)
    if row < 2:
        moves.append(blank + 3)
    if col > 0:
        moves.append(blank - 1)
    if col < 2:
        moves.append(blank + 1)

    for new_blank in moves:
        new_state = state.copy()

        new_state[blank], new_state[new_blank] = \
            new_state[new_blank], new_state[blank]

        successors.append(new_state)

    return successors


def a_star_misplaced(initial, goal):
    open_list = [(initial, 0, misplaced_tiles(initial, goal), [initial])]
    closed = []

    while open_list:

        open_list.sort(key=lambda x: x[1] + x[2])

        state, g, h, path = open_list.pop(0)

        if state == goal:
            return path

        if state in closed:
            continue

        closed.append(state)

        for successor in get_successors(state):

            if successor not in closed:
                new_g = g + 1
                new_h = misplaced_tiles(successor, goal)

                open_list.append(
                    (successor, new_g, new_h, path + [successor])
                )

    return None


def print_path(path):
    if path is None:
        print("No solution")
        return

    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:
        for i in range(9):
            print(state[i], end=" ")

            if i % 3 == 2:
                print()

        print()

print("Shashwat        1BF24CS278")
initial = [2,8,3,1,6,4,7,0,5]

goal = [1,2,3,8,0,4,7,6,5]

path = a_star_misplaced(initial, goal)

print_path(path)
