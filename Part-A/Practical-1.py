A_state = input("Enter initial state for A room (clean/dirty): ").lower()
B_state = input("Enter initial state for B room (clean/dirty): ").lower()
agent_location = input("Enter initial location for agent (A/B): ").upper()

def simple_reflex_agent():
    global A_state, B_state, agent_location

    print("\nCurrent Environment:")
    print(f"A: {A_state}, B: {B_state}, Agent Location: {agent_location}")

    if agent_location == "A":
        percept = A_state
    else:
        percept = B_state

    if percept == "dirty":
        print("Action: SUCK")

        if agent_location == "A":
            A_state = "clean"
        else:
            B_state = "clean"

    if agent_location == "A":
        agent_location = "B"
        print("Action: MOVE TO B")
    else:
        agent_location = "A"
        print("Action: MOVE TO A")

def main():
    while True:
        simple_reflex_agent()

        if A_state == "clean" and B_state == "clean":
            print("\nAction: NO OPERATION")
            print("Agent has finished cleaning.")
            break

if __name__ == "__main__":
    main()
