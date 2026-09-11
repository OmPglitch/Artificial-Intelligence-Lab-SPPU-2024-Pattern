
# Practical 1: Simple Reflex Agent 

def vacuum_agent(location, status):
    # Rule 1: If current location is dirty, clean it
    if status == 1:
        print(f"Location {location} is DIRTY. Action: SUCK")
        status = 0 # Room becomes clean
        print(f"Location {location} is now CLEAN.")
    else:
        print(f"Location {location} is already CLEAN. Action: NO-OP")

    # Rule 2: Movement rule
    if location == 'A':
        print("Action: Move RIGHT to Location B")
        location = 'B'
    elif location == 'B':
        print("Action: Move LEFT to Location A")
        location = 'A'

    return location, status

# Main code
print("--- Vacuum Cleaner Simulation ---")
print("Enter status (1 for Dirty, 0 for Clean)")

# Take inputs from user
loc = input("Enter initial location of agent (A or B): ").upper()
status_a = int(input("Enter status of Room A (0 or 1): "))
status_b = int(input("Enter status of Room B (0 or 1): "))

cost = 0

# Cycle through both rooms once
for step in range(2):
    print(f"\nStep {step + 1}:")
    if loc == 'A':
        loc, status_a = vacuum_agent(loc, status_a)
    else:
        loc, status_b = vacuum_agent(loc, status_b)
    cost += 1

print("\n--- Final Status ---")
print("Room A status:", "Clean" if status_a == 0 else "Dirty")
print("Room B status:", "Clean" if status_b == 0 else "Dirty")
print("Total path cost:", cost)
