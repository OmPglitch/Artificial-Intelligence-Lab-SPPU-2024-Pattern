grid = [
    ["A", 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, "G"]
]

agent_position = [0, 0]
internal_state = []

def model_based_agent():
    global agent_position, internal_state

    row, col = agent_position
    internal_state.append((row, col))

    print("\nCurrent Position:", agent_position)
    print("Visited Positions:", internal_state)

    if agent_position == [3, 3]:
        print("Goal Reached!")
        return False

    possible_moves = [
        (row, col + 1, "MOVE RIGHT"),
        (row + 1, col, "MOVE DOWN"),
        (row, col - 1, "MOVE LEFT"),
        (row - 1, col, "MOVE UP")
    ]

    for new_row, new_col, action in possible_moves:
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] != 1 and (new_row, new_col) not in internal_state:
                agent_position = [new_row, new_col]
                print("Action:", action)
                return True

    print("No path available.")
    return False


def main():
    print("Model-Based Intelligent Agent")
    print("-----------------------------")

    while True:
        if not model_based_agent():
            break


if __name__ == "__main__":
    main()
