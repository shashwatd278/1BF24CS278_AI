import math
import random

N = 8


def calculate_cost(board):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def simulated_annealing(board):
    temperature = 1000.0
    cooling_rate = 0.98  
    min_temperature = 0.01

    current_board = board.copy()
    current_cost = calculate_cost(current_board)

    while temperature > min_temperature:
        if current_cost == 0:
            return current_board

        col1, col2 = random.sample(range(N), 2)
        new_board = current_board.copy()
        new_board[col1], new_board[col2] = new_board[col2], new_board[col1]

        new_cost = calculate_cost(new_board)
        delta = new_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_board = new_board
            current_cost = new_cost

        temperature *= cooling_rate

    return current_board


def display_board(board):
    for row in range(N):
        line = []
        for col in range(N):
            if board[col] == row:
                line.append(" Q ")
            else:
                line.append(" . ")
        print("".join(line))


if __name__ == "__main__":
    print("8-Queens Problem using Simulated Annealing\n")
    print("Enter 8 numbers (0-7) representing queen row indices per column:")

    board = []
    for i in range(N):
        try:
            value = int(input(f"Enter row for queen in column {i}: "))
            if value < 0 or value >= N:
                print("Invalid input! Enter values between 0 and 7.")
                exit(1)
            board.append(value)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            exit(1)

    print("\nInitial Board:")
    display_board(board)
    initial_conflicts = calculate_cost(board)
    print(f"Initial conflicts: {initial_conflicts}")

    solution = simulated_annealing(board)
    final_conflicts = calculate_cost(solution)

    print("\nFinal Board:")
    display_board(solution)
    print(f"Final conflicts: {final_conflicts}")

    if final_conflicts == 0:
        print("\nSuccess: Solution found!")
    else:
        print("\nStuck in local optimum. Try running again or adjusting initial state.")
